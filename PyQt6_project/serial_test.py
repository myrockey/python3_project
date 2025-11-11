# 串口调试上位机 PyQt6 串口上位机 
# 一键打包	pyinstaller -F -w serial_test.py 生成无控制台 exe
# 生成的文件就是 dist/serial_test.exe
import sys, serial, serial.tools.list_ports
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QComboBox,
                             QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout,
                             QLabel, QMessageBox, QCheckBox)
from PyQt6.QtCore import QTimer, pyqtSignal, QObject
from PyQt6.QtSerialPort import QSerialPort, QSerialPortInfo


class SerialWorker(QObject):
    """串口数据转发器：把 readyRead 信号转成 Python 信号"""
    got_data = pyqtSignal(bytes)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.sp = QSerialPort()
        self.sp.readyRead.connect(self._read)

    def _read(self):
        while self.sp.bytesAvailable():
            chunk = self.sp.readAll()
            self.got_data.emit(chunk.data())   # PyQt6 返回 QByteArray


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("rockey串口调试助手V1.0")
        self.resize(700, 500)

        # 中心控件
        central = QWidget()
        self.setCentralWidget(central)
        lay_main = QVBoxLayout(central)

        # 顶部参数区
        lay_top = QHBoxLayout()
        self.cb_port = QComboBox()
        self.cb_baud = QComboBox()
        self.cb_baud.addItems(["9600", "115200", "38400", "19200"])
        self.cb_baud.setCurrentText("9600")
        self.btn_open = QPushButton("打开串口")
        self.btn_refresh = QPushButton("刷新端口")
        lay_top.addWidget(QLabel("端口:"))
        lay_top.addWidget(self.cb_port)
        lay_top.addWidget(QLabel("波特率:"))
        lay_top.addWidget(self.cb_baud)
        lay_top.addWidget(self.btn_open)
        lay_top.addWidget(self.btn_refresh)
        lay_top.addStretch()
        lay_main.addLayout(lay_top)

        # 接收区
        self.te_rx = QTextEdit()
        self.te_rx.setReadOnly(True)
        self.cb_hex_rx = QCheckBox("HEX显示")
        self.btn_clear_rx = QPushButton("清空接收区")
        lay_rx_bar = QHBoxLayout()
        lay_rx_bar.addWidget(QLabel("接收区:"))
        lay_rx_bar.addWidget(self.cb_hex_rx)
        lay_rx_bar.addWidget(self.btn_clear_rx)
        lay_rx_bar.addStretch()
        lay_main.addLayout(lay_rx_bar)
        lay_main.addWidget(self.te_rx)

        # 发送区
        self.te_tx = QTextEdit()
        self.te_tx.setMaximumHeight(80)
        self.cb_newline = QCheckBox("自动加换行")
        self.cb_newline.setChecked(True)
        self.cb_hex_tx = QCheckBox("HEX发送")
        self.btn_send = QPushButton("发送")
        self.btn_clear_tx = QPushButton("清空发送区")
        lay_send = QHBoxLayout()
        lay_send.addWidget(self.te_tx)
        lay_send.addWidget(self.cb_newline)
        lay_send.addWidget(self.cb_hex_tx)
        lay_send.addWidget(self.btn_send)
        lay_send.addWidget(self.btn_clear_tx)
        lay_main.addLayout(lay_send)

        # 串口对象
        self.serial = SerialWorker()
        self.serial.got_data.connect(self.handle_recv)

        # 信号
        self.btn_open.clicked.connect(self.open_close)
        self.btn_send.clicked.connect(self.send_data)
        self.btn_refresh.clicked.connect(self.refresh_port)
        self.btn_clear_rx.clicked.connect(self.te_rx.clear)  # ←清空接收
        self.btn_clear_tx.clicked.connect(self.te_tx.clear)  # ←清空发送

        # 新增：发送按钮默认不可用
        self.btn_send.setEnabled(False)

        # 初始化
        self.refresh_port()

    # ---------- 端口 ----------
    def refresh_port(self):
        self.cb_port.clear()
        ports = [p.portName() for p in QSerialPortInfo.availablePorts()]
        self.cb_port.addItems(ports)

    # ---------- 打开/关闭 ----------
    def open_close(self):
        if self.serial.sp.isOpen():
            self.serial.sp.close()
            self.btn_open.setText("打开串口")
            self.btn_send.setEnabled(False)      # ←关闭后禁用
            return

        self.serial.sp.setPortName(self.cb_port.currentText())
        self.serial.sp.setBaudRate(int(self.cb_baud.currentText()))
        self.serial.sp.setDataBits(QSerialPort.DataBits.Data8)
        self.serial.sp.setParity(QSerialPort.Parity.NoParity)
        self.serial.sp.setStopBits(QSerialPort.StopBits.OneStop)
        self.serial.sp.setFlowControl(QSerialPort.FlowControl.NoFlowControl)

        ok = self.serial.sp.open(QSerialPort.OpenModeFlag.ReadWrite)
        if ok:
            self.btn_open.setText("关闭串口")
            self.btn_send.setEnabled(True)       # ←打开后启用
        else:
            QMessageBox.critical(self, "错误", "无法打开串口！")

    # ---------- 接收 ----------
    def handle_recv(self, data: bytes):
        if self.cb_hex_rx.isChecked():          # === NEW
            hex_str = ' '.join(f'{b:02X}' for b in data)
            self.te_rx.append(hex_str)
        else:
            try:
                text = data.decode('gbk', errors='replace').strip()
            except:
                text = data.decode('utf-8', errors='replace').strip()
            self.te_rx.append(text)

    # ---------- 发送 ----------
    def send_data(self):
        if not self.serial.sp.isOpen():
            QMessageBox.warning(self, "提示", "串口未打开")
            return
        txt = self.te_tx.toPlainText().strip()
        if not txt:
            return
        try:
            if self.cb_hex_tx.isChecked():
                txt = txt.replace(' ', '')
                if len(txt) % 2:  # 奇数个字符
                    txt = txt[:-1] + '0' + txt[-1]  # 再最后一个字符的前面补0
                data = bytes(int(txt[i:i+2], 16) for i in range(0, len(txt), 2))
            else:
                if self.cb_newline.isChecked() and not txt.endswith('\n'):
                    txt += '\n'
                data = txt.encode('gbk', errors='replace')
        except ValueError:
            QMessageBox.critical(self, "错误", "HEX 格式错误！\n只允许 0-9 A-F 字符")
            return
        self.serial.sp.write(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())