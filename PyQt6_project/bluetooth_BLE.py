# 串口SPP调试蓝牙助手 上位机
# 一键打包	pyinstaller -F -w bluetooth_BLE.py 生成无控制台 exe #打包压缩后大小大概35M
# pyinstaller -F -w bluetooth_BLE.py --upx-dir D:\tools\upx-5.0.2-win6  #加了upx打包压缩后大小大概31M 

"""
操作步骤：
1.手机端打开 蓝牙调试工具，点击BLE从机 打开等待
2.电脑端打开 BLE调试工具,扫描-扫描完成后搜索你的蓝牙地址-点击连接-发现6个服务-选择最常用的服务（0000ffe0-0000-1000-8000-00805f9b34fb），右侧选择对应的特征（0000ffe1-0000-1000-8000-00805f9b34fb）
3.手机端，可以看到心跳发送的包内容了，就可以正常通信了，读，写，通知。
读-是读取手机端的包（BLE从机打开的时候设置的响应包内容）
写-是电脑端发送给手机端数据
通知-是手机端发送给电脑端数据

"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python BLE蓝牙调试助手（PyQt6 + bleak）
扫描、连接、服务/特征枚举、读、写、通知
新增：UTF-8/HEX 双模式收发
选 UTF-8+LF 就是帮你“回车”发出去，省得每次手动敲 Enter。
"""
import sys, asyncio, datetime, re, string
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from bleak import BleakClient, BleakScanner
import qasync

# ---------------- 日志输出 ----------------
def log(te: QTextEdit, txt: str):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    te.append(f"[{ts}] {txt}")

# ---------------- 编码/解码工具 ----------------
def _is_utf8_printable(b: bytes) -> bool:
    """简单判断：是否全是可打印 ASCII 或合法 UTF-8 且含可见字符"""
    try:
        s = b.decode('utf-8')
        return all(c in string.printable or ord(c) >= 0xA0 for c in s)
    except UnicodeDecodeError:
        return False

def bytes_to_ui(b: bytes, mode: str) -> str:
    """把字节数组转成 UI 要显示的字符串"""
    if mode == 'HEX':
        return b.hex().upper()
    if mode == 'UTF-8+LF':
        return b.decode('utf-8', errors='replace')
    return b.decode('utf-8', errors='replace').rstrip('\x00')

def ui_to_bytes(s: str, mode: str) -> bytes:
    """把 UI 字符串转成字节数组"""
    s = s.strip()
    if mode == 'HEX':
        s = re.sub(r'\s+', '', s)
        if len(s) % 2:
            s = s[:-1] + '0' + s[-1]
        return bytes(int(s[i:i + 2], 16) for i in range(0, len(s), 2))
    if mode == 'UTF-8+LF' and not s.endswith('\n'):
        s += '\n'
    return s.encode('utf-8')

# ---------------- 主窗口 ----------------
class BleDebugTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("rockey-BLE蓝牙调试助手V1.0")
        self.resize(700, 600)
        self.client: BleakClient | None = None
        self.build_ui()
        self.loop = asyncio.get_event_loop()
        self._hb_timer = QTimer(self)
        self._hb_timer.timeout.connect(self._do_heartbeat)
        self._user_disconnect = False

    # ---------- UI ----------
    def build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        lay = QVBoxLayout(central)

        top = QHBoxLayout()
        self.cb_dev = QComboBox()
        self.btn_scan = QPushButton("扫描")
        self.btn_conn = QPushButton("连接")
        self.btn_disc = QPushButton("断开")
        self.sts = QLabel("就绪")
        top.addWidget(QLabel("设备:"))
        top.addWidget(self.cb_dev, 2)
        top.addWidget(self.btn_scan)
        top.addWidget(self.btn_conn)
        top.addWidget(self.btn_disc)
        top.addWidget(self.sts)
        lay.addLayout(top)

        search_lay = QHBoxLayout()
        search_lay.addWidget(QLabel("搜索:"))
        self.search_le = QLineEdit()
        self.search_le.setClearButtonEnabled(True)
        self.search_le.textChanged.connect(self.filter_devices)
        search_lay.addWidget(self.search_le)
        lay.insertLayout(1, search_lay)

        self._dev_cache = []

        mid = QHBoxLayout()
        self.srv_list = QListWidget()
        self.srv_list.setMaximumWidth(250)
        self.char_list = QListWidget()
        mid.addWidget(QLabel("服务"))
        mid.addWidget(self.srv_list)
        mid.addWidget(QLabel("特征"))
        mid.addWidget(self.char_list)
        lay.addLayout(mid)

        log_bar = QHBoxLayout()
        log_bar.addWidget(QLabel("日志"))
        self.btn_clear_log = QPushButton("清除")
        log_bar.addStretch()
        log_bar.addWidget(self.btn_clear_log)
        lay.addLayout(log_bar)
        self.log_te = QTextEdit(readOnly=True)
        lay.addWidget(self.log_te)

        bot = QHBoxLayout()
        self.data_le = QLineEdit("Hello 世界")  # 默认 UTF-8 文本
        self.mode_cb = QComboBox()
        self.mode_cb.addItems(['UTF-8', 'UTF-8+LF', 'HEX'])
        self.mode_cb.setMaximumWidth(90)
        self.btn_read = QPushButton("读")
        self.btn_write = QPushButton("写")
        self.btn_notify = QCheckBox("通知")
        bot.addWidget(self.data_le, 2)
        bot.addWidget(self.mode_cb)
        bot.addWidget(self.btn_read)
        bot.addWidget(self.btn_write)
        bot.addWidget(self.btn_notify)
        lay.addLayout(bot)

        # 信号
        self.btn_scan.clicked.connect(self.scan)
        self.btn_conn.clicked.connect(self.connect)
        self.btn_disc.clicked.connect(self.disconnect)
        self.btn_read.clicked.connect(self.read_char)
        self.btn_write.clicked.connect(self.write_char)
        self.btn_notify.toggled.connect(self.notify_switch)
        self.srv_list.itemClicked.connect(self.on_srv_click)
        self.char_list.itemClicked.connect(self.on_char_click)
        self.btn_clear_log.clicked.connect(lambda: self.log_te.clear())

    # ---------- 过滤 ----------
    def filter_devices(self):
        kw = self.search_le.text().strip().lower()
        self.cb_dev.clear()
        for text, addr in self._dev_cache:
            if kw in text.lower() or kw in addr.lower():
                self.cb_dev.addItem(text, addr)

    # ---------- 心跳 ----------
    @qasync.asyncSlot()
    async def _do_heartbeat(self):
        if not (self.client and self.client.is_connected):
            return
        char = getattr(self, 'current_char', None)
        if char is None or 'write' not in char.properties:
            return
        try:
            await self.client.write_gatt_char(char.uuid, b'\x00', response=True)
            log(self.log_te, "心跳写 OK")
        except Exception as e:
            log(self.log_te, f"心跳失败：{e}")
            self._hb_timer.stop()

    # ---------- 扫描 ----------
    @qasync.asyncSlot()
    async def scan(self):
        log(self.log_te, "开始扫描...")
        self.cb_dev.clear()
        self._dev_cache.clear()
        devices = await BleakScanner.discover(timeout=5.0, scanning_mode="active")
        for d in devices:
            name = d.name or f"Unnamed-{d.address[-5:].replace(':', '')}"
            self._dev_cache.append((f"{name}  [{d.address}]", d.address))
        self.filter_devices()
        log(self.log_te, f"扫描完成，共 {len(self._dev_cache)} 台")

    # ---------- 连接 ----------
    @qasync.asyncSlot()
    async def connect(self):
        addr = self.cb_dev.currentData()
        if not addr:
            log(self.log_te, "请先选择设备")
            return
        log(self.log_te, f"正在连接 {addr} ...")
        self.client = BleakClient(addr, disconnected_callback=self.on_ble_disconnect, timeout=20.0)
        try:
            await self.client.connect()
            log(self.log_te, "已连接")
            self.sts.setText("已连接")
            await self.enum_services()
            self._hb_timer.start(3_000)
        except Exception as e:
            log(self.log_te, f"连接失败：{type(e).__name__} - {e}")
            self.sts.setText("连接失败")

    def on_ble_disconnect(self, client: BleakClient):
        log(self.log_te, "★ BLE 已断开")
        self.sts.setText("已断开")
        self._hb_timer.stop()
        if not self._user_disconnect:
            QTimer.singleShot(500, lambda: self.connect())
            self._user_disconnect = False

    # ---------- 断开 ----------
    @qasync.asyncSlot()
    async def disconnect(self):
        self._user_disconnect = True
        if self.client and self.client.is_connected:
            await self.client.disconnect()
            log(self.log_te, "电脑端主动断开")
        self.client = None
        self.sts.setText("就绪")
        self.srv_list.clear()
        self.char_list.clear()
        self.current_char = None

    # ---------- 枚举 ----------
    async def enum_services(self):
        self.srv_list.clear()
        self.char_list.clear()
        services = list(self.client.services)
        log(self.log_te, f"发现 {len(services)} 个服务")
        for srv in services:
            item = QListWidgetItem(f"{srv.uuid}")
            item.setData(Qt.ItemDataRole.UserRole, srv)
            self.srv_list.addItem(item)

    def on_srv_click(self, item):
        srv = item.data(Qt.ItemDataRole.UserRole)
        self.char_list.clear()
        for char in srv.characteristics:
            props = ",".join(char.properties)
            item = QListWidgetItem(f"{char.uuid}  [{props}]")
            item.setData(Qt.ItemDataRole.UserRole, char)
            self.char_list.addItem(item)

    def on_char_click(self, item):
        char = item.data(Qt.ItemDataRole.UserRole)
        self.current_char = char
        log(self.log_te, f"选中特征 {char.uuid}")
        if 'write' in char.properties:
            self._hb_timer.start(3_000)
            log(self.log_te, "心跳已启动")
        else:
            log(self.log_te, "当前特征不可写，心跳保持停止")

    # ---------- 读 ----------
    @qasync.asyncSlot()
    async def read_char(self):
        if not hasattr(self, 'current_char'):
            log(self.log_te, "请先选择特征")
            return
        if not self.client or not self.client.is_connected:
            log(self.log_te, "链路已断，请先重连")
            return
        try:
            data = await self.client.read_gatt_char(self.current_char.uuid)
            mode = self.mode_cb.currentText()
            text = bytes_to_ui(data, mode)
            # 日志区同时给出两种视图
            if mode == 'HEX':
                log(self.log_te, f"读取成功（HEX）：{data.hex()}")
            elif not _is_utf8_printable(data):
                log(self.log_te, f"读取成功（HEX）：{data.hex()}")
            else:
                log(self.log_te, f"读取成功：{text}")
        except Exception as e:
            log(self.log_te, f"读取失败：{e}")

    # ---------- 写 ----------
    @qasync.asyncSlot()
    async def write_char(self):
        if not hasattr(self, 'current_char'):
            log(self.log_te, "请先选择特征")
            return
        txt = self.data_le.text()
        mode = self.mode_cb.currentText()
        try:
            data = ui_to_bytes(txt, mode)
            await self.client.write_gatt_char(self.current_char.uuid, data)
            if mode == 'HEX':
                log(self.log_te, f"写入成功（HEX）：{data.hex()}")
            else:
                log(self.log_te, f"写入成功：{txt}")
        except Exception as e:
            log(self.log_te, f"写入失败：{e}")

    # ---------- 通知 ----------
    @qasync.asyncSlot(bool)
    async def notify_switch(self, on: bool):
        if not hasattr(self, 'current_char'):
            self.btn_notify.setChecked(False)
            log(self.log_te, "请先选择特征")
            return
        try:
            if on:
                await self.client.start_notify(self.current_char.uuid, self.notify_callback)
                log(self.log_te, "已打开通知")
            else:
                await self.client.stop_notify(self.current_char.uuid)
                log(self.log_te, "已关闭通知")
        except Exception as e:
            log(self.log_te, f"通知开关失败：{e}")
            self.btn_notify.setChecked(False)

    def notify_callback(self, handle: int, data: bytearray):
        mode = self.mode_cb.currentText()
        text = bytes_to_ui(data, mode)
        if mode == 'HEX':
            log(self.log_te, f"[通知]（HEX）{data.hex()}")
        elif not _is_utf8_printable(data):
            log(self.log_te, f"[通知]（HEX）{data.hex()}")
        else:
            log(self.log_te, f"[通知] {text}")


# ---------------- 入口 ----------------
def main():
    app = QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    asyncio.set_event_loop(loop)

    w = BleDebugTool()
    w.show()

    with loop:
        loop.run_forever()


if __name__ == '__main__':
    main()