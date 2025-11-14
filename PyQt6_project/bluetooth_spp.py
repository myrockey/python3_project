# 串口SPP调试蓝牙助手 上位机
# 一键打包	pyinstaller -F -w bluetooth_spp.py 生成无控制台 exe #打包压缩后大小大概35M
# pyinstaller -F -w bluetooth_spp.py --upx-dir D:\tools\upx-5.0.2-win6  #加了upx打包压缩后大小大概31M 

# 1 手机端打开蓝牙调试宝-服务端模式(SPP Server)-设置自动应答，以及接收编码模式为utf-8或其他格式
# 2.电脑端打开蓝牙，并和手机的蓝牙配对，配对成功并显示未连接或已连接，必须查看电脑端-蓝牙设置-com端口-发现 SPP 或 Classic 字样 等相关的端口，说明spp蓝牙配对成功并连接了com端口可以通过串口传输数据了。
# 3.电脑端打开spp蓝牙助手软件，下拉选择对应com端口，并点击按钮打开，并接收到手机端的成功应答，说明连接手机蓝牙成功,可以进行电脑和手机的串口数据传输了。
import sys
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QPushButton,
    QComboBox, QHBoxLayout, QVBoxLayout, QWidget, QLabel, QProgressBar
)
from PyQt6.QtCore import QIODevice,QTimer
# 仅新增 QtSerialPort
from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo


class BluetoothSPPGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("rockey-串口SPP调试蓝牙助手")
        self.resize(700, 500)
        self.socket = None          # 现在指向 QSerialPort，保持原名防改动
        self.build_ui()
        self.populate_com_ports()
        self.progress.hide()        # 串口无需滚动条

    # ---------- UI ----------
    def build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        lay = QVBoxLayout(central)

        top = QHBoxLayout()
        self.cb_devices = QComboBox()          # 现在放 COM 口
        self.btn_scan = QPushButton("刷新串口")
        self.btn_conn = QPushButton("打开")
        self.status_lbl = QLabel("就绪")
        self.progress = QProgressBar()
        self.progress.setRange(0, 0)
        self.progress.hide()
        top.addWidget(QLabel("串口:"))
        top.addWidget(self.cb_devices, 2)
        top.addWidget(self.btn_scan)
        top.addWidget(self.btn_conn)
        top.addWidget(self.status_lbl)
        top.addWidget(self.progress)
        lay.addLayout(top)

        self.te_rx = QTextEdit()
        self.te_rx.setReadOnly(True)
        lay.addWidget(QLabel("接收区:"))
        lay.addWidget(self.te_rx)

        self.te_tx = QTextEdit()
        self.te_tx.setMaximumHeight(80)
        self.btn_send = QPushButton("发送")
        lay.addWidget(QLabel("发送区:"))
        lay.addWidget(self.te_tx)
        lay.addWidget(self.btn_send)

        self.btn_scan.clicked.connect(self.populate_com_ports)
        self.btn_conn.clicked.connect(self.connect_device)
        self.btn_send.clicked.connect(self.send_data)

    # ---------- 日志 ----------
    def log(self, s):
        ts = datetime.now().strftime("%H:%M:%S")
        self.te_rx.append(f"[{ts}] {s}")

    # ---------- 串口列表 ----------
    def populate_com_ports(self):
        self.cb_devices.clear()
        for info in QSerialPortInfo.availablePorts():
            self.cb_devices.addItem(f"{info.portName()}  ({info.description()})", info)
        self.log(f"刷新串口，共 {self.cb_devices.count()} 个")

    # ---------- 打开/关闭串口 ----------
    def connect_device(self):
        # 如果已打开，则关闭
        if self.socket and self.socket.isOpen():
            self.log("关闭串口...")
            self.socket.close()          # 会触发 _on_disconnected
            return

        info = self.cb_devices.currentData()
        if not info:
            self.log("请先选择串口")
            return

        # 新建串口对象
        self.socket = QSerialPort(info)
        self.socket.setBaudRate(115200)
        self.socket.readyRead.connect(self.read_data)
        self.socket.errorOccurred.connect(self._on_error)
        # 关键：让 close() 触发 _on_disconnected
        self.socket.aboutToClose.connect(self._on_disconnected)

        ok = self.socket.open(QIODevice.OpenModeFlag.ReadWrite)
        if ok:
            self._on_connected()
        else:
            self._on_error(self.socket.error())

    # ---------- 信号槽 ----------
    def _on_connected(self):
        self.log("串口已打开，等待对端响应...")
        self.status_lbl.setText("等待握手")
        self.btn_conn.setText("关闭")
        self.socket.write(b'{"cmd":"hello"}\n')
        # 用实例变量保存 QTimer，方便后面停掉
        self.hello_timer = QTimer(self)
        self.hello_timer.timeout.connect(self._hello_timeout)
        self.hello_timer.setSingleShot(True)
        self.hello_timer.start(2000)

    def _hello_timeout(self):
        if self.socket and self.socket.isOpen() and self.status_lbl.text() == "等待握手":
            self.log("超时：串口已开，但未收到手机回应，请确认手机蓝牙SPP已连接")
            self.status_lbl.setText("未握手")

    def _on_disconnected(self):
        if self.socket:
            # self.socket.close()      # ← 就是这行导致闭环，删掉
            self.socket.deleteLater()
            self.socket = None
        self.log("串口已关闭")
        self.status_lbl.setText("就绪")
        self.btn_conn.setText("打开")

    def _on_error(self, err):
        self.log(f"串口错误: {self.socket.errorString()}")
        self.status_lbl.setText("错误")

    # ---------- 收发 ----------
    def read_data(self):
        if not self.socket:
            return
        data = self.socket.readAll()
        if not data:
            return
        text = data.data().decode('utf-8', errors='ignore')
        self.te_rx.append(text)
        if self.status_lbl.text() == "等待握手":
            self.log("收到数据，手机侧已连接")
            self.status_lbl.setText("已连接")
            if self.hello_timer and self.hello_timer.isActive():
                self.hello_timer.stop()

    def send_data(self):
        if not self.socket or not self.socket.isOpen():
            self.log("串口未打开"); return
        txt = self.te_tx.toPlainText()
        if not txt:
            return
        self.socket.write(txt.encode('utf-8'))
        self.te_tx.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = BluetoothSPPGui()
    w.show()
    sys.exit(app.exec())