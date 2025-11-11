#!/usr/bin/python3

'''
PyQt6 的交互核心是 “信号与槽（Signal and Slot）” 机制，组件的动作（如点击、输入、选择）会发出 “信号”，开发者通过绑定 “槽函数” 来响应这些信号，实现交互逻辑。

5.1 信号与槽的基本使用
方式 1：直接绑定槽函数
'''
def test1():
    from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(300, 200)
    
    layout = QVBoxLayout(window)
    
    # 定义槽函数
    def on_click():
        print("按钮被点击了！")
    
    # 创建按钮，绑定信号与槽
    btn = QPushButton("点击我")
    btn.clicked.connect(on_click)  # clicked是信号，connect绑定槽函数
    layout.addWidget(btn)
    
    window.show()
    sys.exit(app.exec())

# test1()

'''
方式 2：带参数的槽函数
'''
def test2():
    from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QLabel
    from PyQt6.QtCore import Qt
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(300, 200)
    
    layout = QVBoxLayout(window)
    label = QLabel("当前值：50")
    layout.addWidget(label)
    
    # 带参数的槽函数
    def on_value_change(value):
        label.setText(f"当前值：{value}")
    
    # 滑块值变化信号（带参数）绑定槽函数
    slider = QSlider(Qt.Orientation.Horizontal)
    slider.setRange(0, 100)
    slider.setValue(50)
    slider.valueChanged.connect(on_value_change)  # valueChanged信号传递数值参数
    layout.addWidget(slider)
    
    window.show()
    sys.exit(app.exec())

# test2()

'''
方式 3：解除信号与槽的绑定
'''
def test3():
    from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(300, 200)
    
    layout = QVBoxLayout(window)
    
    def on_click():
        print("按钮被点击了！")
        # 解除绑定，后续点击不再触发
        btn.clicked.disconnect(on_click)
    
    btn = QPushButton("点击一次")
    btn.clicked.connect(on_click)
    layout.addWidget(btn)
    
    window.show()
    sys.exit(app.exec())

# test3()

'''
5.2 常用组件的核心信号
组件	信号名称	说明
QPushButton	clicked()	按钮被点击时发出
QLineEdit	textChanged(text)	文本内容变化时发出（带文本参数）
QCheckBox	stateChanged(state)	勾选状态变化时发出（带状态参数）
QRadioButton	toggled(checked)	勾选状态变化时发出（带布尔参数）
QComboBox	currentIndexChanged(index)	选择项变化时发出（带索引参数）
QSlider	valueChanged(value)	滑块值变化时发出（带数值参数）
QListWidget	itemClicked(item)	列表项被点击时发出（带项参数）
5.3 自定义信号与槽
除了组件自带的信号，还可以自定义信号，实现更灵活的事件传递。

示例：自定义信号
'''
def test4():
    from PyQt6.QtCore import QObject, pyqtSignal
    from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
    import sys
    
    # 自定义信号类（必须继承QObject）
    class MySignal(QObject):
        # 定义自定义信号（可带参数）
        custom_signal = pyqtSignal(str)
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(300, 200)
    
    layout = QVBoxLayout(window)
    
    # 创建信号实例
    signal = MySignal()
    
    # 定义槽函数
    def on_custom_signal(msg):
        print(f"收到自定义信号：{msg}")
    
    # 绑定自定义信号与槽
    signal.custom_signal.connect(on_custom_signal)
    
    # 按钮点击时发射自定义信号
    def send_signal():
        signal.custom_signal.emit("Hello, 自定义信号！")
    
    btn = QPushButton("发射信号")
    btn.clicked.connect(send_signal)
    layout.addWidget(btn)
    
    window.show()
    sys.exit(app.exec())

# test4()
