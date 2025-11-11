"""
PyQt6 提供了上百种组件，以下是最常用的 10 种核心组件，每种都包含 “功能说明 + 代码示例 + 参数解析”，可直接套用。

3.1 窗口（QWidget/QMainWindow）
窗口是应用的容器，PyQt6 中常用QWidget（基础窗口）和QMainWindow（带菜单栏 / 工具栏的主窗口）。

示例：基础窗口配置
————————————————
版权声明：本文为CSDN博主「猿大叔~」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/toungboy/article/details/154354031
"""

#示例：基础窗口配置
def test1():
    from PyQt6.QtWidgets import QApplication,QWidget
    from PyQt6.QtGui import QIcon
    import sys,os

    # 1. 创建应用实例（每个PyQt程序必须有且只有一个QApplication）
    app = QApplication(sys.argv)

    # 2.创建基础窗口
    window = QWidget()
    window.setWindowTitle("PyQt6窗口示例") # 窗口标题
    window.resize(500,400) # 窗口大小（宽X高）
    window.move(100,100) # 窗口初始位置（屏幕左上角为原点 0,0）
    window.setFixedSize(500,400) # 禁止调整窗口大小

    # 设置窗口图标（需.ico文件）
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    window.setWindowIcon(QIcon(exec_path + "/test1_icon.ico"))

    # 3.添加组件

    # 4.显示窗口
    window.show()

    # 5.启动应用事件循环
    sys.exit(app.exec())

# test1()

# QMainWindow：带菜单栏的主窗口
def test2():
    from PyQt6.QtWidgets import QApplication,QWidget,QMainWindow
    import sys

    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("QMainWindow示例") # 窗口标题
            self.resize(500,400) # 窗口大小 宽x高
            # 设置中心组件（QMainWindow必需通过中心组件添加内容）
            self.setCentralWidget(QWidget())
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

# test2()

'''
3.2 标签（QLabel）：显示文本或图片
QLabel 用于显示静态文本、图片或富文本，是最基础的展示组件。

示例 1：显示文本和富文本
'''
def test3():
    from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
    from PyQt6.QtCore import Qt
    import sys

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QLabel标签示例")
    window.resize(300,200)

    # 创建布局
    layout = QVBoxLayout(window)
    # 1.普通文本标签
    label1 = QLabel("普通文本标签")
    label1.setStyleSheet("font-size:14px;color:#333;") # 设置样式
    layout.addWidget(label1)
    # 2.富文本标签（支持html格式）
    label2 = QLabel('<font color="red" size="5">富文本标签</font>')
    layout.addWidget(label2)
    # 3.居中对齐的标签
    label3 = QLabel("居中对齐的标签")
    label3.setAlignment(Qt.AlignmentFlag.AlignCenter) # 居中对齐
    label3.setStyleSheet("color:#000000;background-color:#f0f0f0;padding:10px;")
    layout.addWidget(label3)

    window.show()
    sys.exit(app.exec())

# test3()

# 示例 2：显示图片
def test4():
    from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
    from PyQt6.QtGui import QPixmap
    from PyQt6.QtCore import Qt
    import sys,os

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("显示图片")
    window.resize(300,300)

    layout = QVBoxLayout(window)

    # 创建图片标签
    label = QLabel()
    # 加载图片（支持图片格式）
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    pixmap = QPixmap(exec_path +"/test.jpg")
    # 缩放图片以适应标签大小
    pixmap = pixmap.scaled(200,200)
    label.setPixmap(pixmap)
    label.setAlignment(Qt.AlignmentFlag.AlignCenter) # 图片居中

    layout.addWidget(label)

    window.show()
    sys.exit(app.exec())

# test4()

'''
3.3 按钮（QPushButton）：触发交互事件
QPushButton 是最常用的交互组件，用户点击后会触发预设的功能逻辑。

基础示例：点击按钮弹出提示
'''
def test5():
    from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QMessageBox
    from PyQt6.QtCore import Qt
    import sys

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QPushButton示例")
    window.resize(300,200)

    layout = QVBoxLayout(window)

    # 定义按钮点击事件的处理函数
    def on_button_click():
        QMessageBox.information(window,"提示","你点击了按钮！") # 弹窗信息框
    
    # 创建按钮
    button = QPushButton("点击我")
    button.setStyleSheet("""
        QPushButton {
            font-size: 14px;
            padding: 8px 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
    """) # 自定义按钮样式(hover为鼠标悬浮效果)
    button.clicked.connect(on_button_click) # 绑定点击事件

    layout.addWidget(button,alignment=Qt.AlignmentFlag.AlignCenter)

    window.show()
    sys.exit(app.exec())

# test5()

# 进阶：按钮状态控制与图标按钮
'''
QHBoxLayout QVBoxLayout 差别

一句话记住：
布局类	排列方向	记忆口诀
QHBoxLayout	水平一行（Horizontal）	先左后右 
QVBoxLayout	垂直一列（Vertical）	先上后下 

QHBoxLayout          QVBoxLayout
┌─[1][2][3]─┐        ┌─[1]───┐
│           │        │ [2]   │
└───────────┘        │ [3]   │
                     └───────┘

'''
def test6():
    from PyQt6.QtWidgets import QApplication,QWidget,QPushButton,QHBoxLayout
    from PyQt6.QtGui import QIcon
    from PyQt6.QtCore import QSize
    import sys,os

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("按钮进阶示例")
    window.resize(300,100)

    layout = QHBoxLayout(window)
    layout.setSpacing(20) # 组件间距

    # 1.带图标的按钮
    icon_btn = QPushButton()
    exec_path = os.path.dirname(__file__)  # 当前正在执行的脚本/可执行文件的绝对路径
    icon_btn.setIcon(QIcon(exec_path + "/icon.jpg")) # 设置图标
    icon_btn.setIconSize(QSize(32,32)) # 图标大小
    layout.addWidget(icon_btn)

    # 2.禁用状态的按钮
    disabled_btn = QPushButton("禁用按钮")
    disabled_btn.setDisabled(True) # 禁用按钮
    layout.addWidget(disabled_btn)

    # 3.切换按钮状态
    toggle_btn = QPushButton("切换状态")
    toggle_btn.setCheckable(True) #可勾选状态
    def on_toggle(state):
        print(f"按钮状态：{'勾选' if state else '未勾选'}")
    
    toggle_btn.toggled.connect(on_toggle) # 绑定状态切换事件
    layout.addWidget(toggle_btn)

    window.show()
    sys.exit(app.exec())

# test6()

'''
3.4 输入框（QLineEdit）：获取单行文本输入
QLineEdit 用于接收用户的单行文本输入（如用户名、密码、搜索关键词），支持输入验证和格式限制。

示例：登录窗口的用户名和密码输入
'''
def test7():
    from PyQt6.QtWidgets import QApplication,QWidget,QLineEdit,QLabel,QVBoxLayout,QPushButton,QMessageBox
    import sys

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("登录窗口")
    window.resize(300,250)
    
    layout = QVBoxLayout(window)
    layout.setSpacing(15)
    layout.setContentsMargins(30,30,30,30) # 内边距

    # 用户名标签和输入框
    user_label = QLabel("用户名：")
    user_label.setStyleSheet("font-size:14px;")
    layout.addWidget(user_label)

    user_edit = QLineEdit()
    user_edit.setPlaceholderText("请输入用户名") # 提示文本
    user_edit.setStyleSheet("font-size:14px;padding:8px;")
    layout.addWidget(user_edit)

    # 密码标签和输入框
    pwd_label = QLabel("密码：")
    pwd_label.setStyleSheet("font-size:14px;")
    layout.addWidget(pwd_label)

    pwd_edit = QLineEdit()
    pwd_edit.setPlaceholderText("请输入密码")
    pwd_edit.setEchoMode(QLineEdit.EchoMode.Password) # 密码隐藏模式
    pwd_edit.setStyleSheet("font-size:14px;padding:8px;")
    layout.addWidget(pwd_edit)

    # 登录按钮
    def login():
        username = user_edit.text().strip()
        password = pwd_edit.text().strip()
        if username == 'admin' and password == '123456':
            QMessageBox.information(window,"成功","登录成功！")
        else:
            QMessageBox.information(window,"错误","用户名或密码错误！")
    
    login_btn = QPushButton("登录")
    login_btn.setStyleSheet("""
        QPushButton {
            font-size: 14px;
            padding: 10px;
            background-color: #2196F3;
            color: white;
            border: none;
            border-radius: 4px;
        }
    """)

    login_btn.clicked.connect(login)
    layout.addWidget(login_btn)

    window.show()
    sys.exit(app.exec())

# test7()

'''
3.5 文本框（QTextEdit）：获取多行文本输入
QTextEdit 支持多行文本输入和编辑，可用于显示日志、编辑文档等场景，支持富文本格式。

示例：文本编辑与内容获取
'''
def test8():
    from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QMessageBox
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QTextEdit示例")
    window.resize(400, 300)

    layout = QVBoxLayout(window)

    # 创建文本框
    text_edit = QTextEdit()
    text_edit.setPlaceholderText("请输入多行文本...")
    text_edit.setStyleSheet("font-size:14px;padding:10px;")
    # 插入默认文本（支持富文本）
    text_edit.insertHtml("<font color='blue'>这是默认的富文本内容</font>")
    layout.addWidget(text_edit)

    # 按钮：获取文本内容
    def get_text():
        # 获取纯文本
        plain_text = text_edit.toPlainText()
        # 获取富文本
        html_text = text_edit.toHtml()
        QMessageBox.information(window, "文本内容", f"纯文本：\n{plain_text}\n\n富文本：\n{html_text[:1000]}...")
    
    get_btn = QPushButton("获取文本")
    get_btn.clicked.connect(get_text)
    layout.addWidget(get_btn)

    window.show()
    sys.exit(app.exec())

# test8()

'''
3.6 复选框（QCheckBox）：多选功能
QCheckBox 用于实现多选功能，用户可勾选多个选项，常用于设置偏好、选择兴趣等场景。

示例：兴趣爱好选择
'''
def test9():
    from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QVBoxLayout, QLabel
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QCheckBox示例")
    window.resize(300, 200)
    
    layout = QVBoxLayout(window)
    
    # 定义变量存储选择结果
    hobbies = []
    
    # 复选框：编程
    cb1 = QCheckBox("编程")
    cb1.setStyleSheet("font-size: 14px;")
    layout.addWidget(cb1)
    
    # 复选框：阅读
    cb2 = QCheckBox("阅读")
    cb2.setStyleSheet("font-size: 14px;")
    layout.addWidget(cb2)
    
    # 复选框：运动
    cb3 = QCheckBox("运动")
    cb3.setStyleSheet("font-size: 14px;")
    layout.addWidget(cb3)
    
    # 显示选择结果
    result_label = QLabel("你的兴趣：")
    result_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
    layout.addWidget(result_label)
    
    def show_result():
        hobbies.clear()
        if cb1.isChecked():
            hobbies.append(cb1.text())
        if cb2.isChecked():
            hobbies.append(cb2.text())
        if cb3.isChecked():
            hobbies.append(cb3.text())
        result_label.setText(f"你的兴趣：{'、'.join(hobbies) if hobbies else '无'}")
    
    # 绑定状态变化事件
    cb1.stateChanged.connect(show_result)
    cb2.stateChanged.connect(show_result)
    cb3.stateChanged.connect(show_result)
    
    window.show()
    sys.exit(app.exec())

# test9()

'''
3.7 单选按钮（QRadioButton）：单选功能
QRadioButton 用于实现单选功能，同一组中只能勾选一个选项，常用于选择性别、学历等场景。

示例：性别选择
'''
def test10():
    from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout, QLabel, QGroupBox
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QRadioButton示例")
    window.resize(300, 200)
    
    layout = QVBoxLayout(window)
    
    # 创建分组框（将单选按钮分组，确保互斥）
    group_box = QGroupBox("选择性别")
    group_box.setStyleSheet("font-size: 14px;")
    group_layout = QVBoxLayout(group_box)
    
    # 单选按钮：男
    rb1 = QRadioButton("男")
    rb1.setStyleSheet("font-size: 14px;")
    rb1.setChecked(True)  # 默认勾选
    group_layout.addWidget(rb1)
    
    # 单选按钮：女
    rb2 = QRadioButton("女")
    rb2.setStyleSheet("font-size: 14px;")
    group_layout.addWidget(rb2)
    
    layout.addWidget(group_box)
    
    # 显示选择结果
    result_label = QLabel("你的性别：男")
    result_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
    layout.addWidget(result_label)
    
    def show_gender():
        if rb1.isChecked():
            result_label.setText("你的性别：男")
        else:
            result_label.setText("你的性别：女")
    
    # 绑定状态变化事件
    rb1.toggled.connect(show_gender)
    rb2.toggled.connect(show_gender)
    
    window.show()
    sys.exit(app.exec())

# test10()

'''
3.8 下拉菜单（QComboBox）：选择预设选项
QComboBox 提供下拉选择列表，用户从预设选项中选择一个，常用于选择城市、年级、文件类型等场景。

示例：城市选择
'''
def test11():
    from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QLabel
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QComboBox示例")
    window.resize(300, 200)
    
    layout = QVBoxLayout(window)
    
    # 创建下拉菜单
    combo = QComboBox()
    combo.setStyleSheet("font-size: 14px; padding: 8px;")
    # 添加选项
    combo.addItems(["北京", "上海", "广州", "深圳", "杭州"])
    # 设置默认选项（索引从0开始）
    combo.setCurrentIndex(0)
    layout.addWidget(combo)
    
    # 显示选择结果
    result_label = QLabel(f"你选择的城市：{combo.currentText()}")
    result_label.setStyleSheet("font-size: 14px; margin-top: 20px;")
    layout.addWidget(result_label)
    
    # 绑定选项变化事件
    def on_combo_change(index):
        result_label.setText(f"你选择的城市：{combo.itemText(index)}")
    
    combo.currentIndexChanged.connect(on_combo_change)
    
    window.show()
    sys.exit(app.exec())

# test11()

'''
3.9 滑块（QSlider）：调节数值
QSlider 用于让用户通过拖动滑块调节数值，常用于调节音量、亮度、字体大小等场景。

示例：调节字体大小
'''
def test12():
    from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout, QLabel
    from PyQt6.QtCore import Qt
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QSlider示例")
    window.resize(300, 200)
    
    layout = QVBoxLayout(window)
    
    # 创建滑块（水平方向）
    slider = QSlider(Qt.Orientation.Horizontal)
    slider.setRange(10, 30)  # 数值范围
    slider.setValue(14)  # 默认值
    slider.setSingleStep(1)  # 步长
    layout.addWidget(slider)
    
    # 显示调节结果
    label = QLabel("当前字体大小：14px")
    label.setStyleSheet("font-size: 14px; margin-top: 20px;")
    layout.addWidget(label)
    
    # 绑定滑块值变化事件
    def on_slider_change(value):
        label.setText(f"当前字体大小：{value}px")
        label.setStyleSheet(f"font-size: {value}px; margin-top: 20px;")
    
    slider.valueChanged.connect(on_slider_change)
    
    window.show()
    sys.exit(app.exec())

# test12()

'''
3.10 列表框（QListWidget）：展示列表数据
QListWidget 用于展示单列列表数据，支持单选、多选和双击事件，常用于展示文件列表、选项列表等。

示例：文件列表展示与选择
'''
def test13():
    from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem, QVBoxLayout, QLabel
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QListWidget示例")
    window.resize(300, 200)
    
    layout = QVBoxLayout(window)
    
    # 创建列表框
    list_widget = QListWidget()
    list_widget.setStyleSheet("font-size: 14px;")
    # 设置选择模式：多选
    list_widget.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
    
    # 添加列表项
    items = ["文件1.txt", "文件2.jpg", "文件3.pdf", "文件4.exe"]
    for item_text in items:
        QListWidgetItem(item_text, list_widget)
    
    layout.addWidget(list_widget)
    
    # 显示选择结果
    result_label = QLabel("你选择的文件：无")
    result_label.setStyleSheet("font-size: 14px; margin-top: 10px;")
    layout.addWidget(result_label)
    
    # 绑定选择变化事件
    def on_list_select():
        selected_items = list_widget.selectedItems()
        selected_texts = [item.text() for item in selected_items]
        result_label.setText(f"你选择的文件：{'、'.join(selected_texts) if selected_texts else '无'}")
    
    list_widget.itemSelectionChanged.connect(on_list_select)
    
    window.show()
    sys.exit(app.exec())

# test13()