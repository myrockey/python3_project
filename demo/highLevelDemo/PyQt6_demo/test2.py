#!/usr/bin/python3

'''
PyQt6 提供三种核心布局方式，用于控制组件在窗口中的位置和大小，避免手动计算坐标的繁琐，确保窗口大小变化时组件能自适应调整。

4.1 垂直布局（QVBoxLayout）：组件垂直排列
QVBoxLayout 将组件按垂直方向依次排列，适合需要上下布局的场景（如表单、列表）。

示例：垂直布局的表单

原文链接：https://blog.csdn.net/toungboy/article/details/154354031
'''
def test1():
    from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
    from PyQt6.QtCore import Qt
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QVBoxLayout示例")
    window.resize(300, 250)
    
    # 创建垂直布局
    layout = QVBoxLayout(window)
    layout.setSpacing(15)  # 组件之间的间距
    layout.setContentsMargins(20, 20, 20, 20)  # 布局与窗口的内边距
    
    # 添加组件
    layout.addWidget(QLabel("用户名："))
    layout.addWidget(QLineEdit())
    
    layout.addWidget(QLabel("密码："))
    layout.addWidget(QLineEdit())
    
    layout.addWidget(QLabel("邮箱："))
    layout.addWidget(QLineEdit())
    
    # 按钮：添加到布局底部，居中对齐
    login_btn = QPushButton("注册")
    layout.addWidget(login_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    
    window.show()
    sys.exit(app.exec())

# test1()

'''
4.2 水平布局（QHBoxLayout）：组件水平排列
QHBoxLayout 将组件按水平方向依次排列，适合需要左右布局的场景（如工具栏、按钮组）。

示例：水平布局的按钮组
'''
def test2():
    from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QHBoxLayout示例")
    window.resize(300, 100)
    
    # 创建水平布局
    layout = QHBoxLayout(window)
    layout.setSpacing(10)
    layout.setContentsMargins(20, 20, 20, 20)
    
    # 添加按钮
    layout.addWidget(QPushButton("新建"))
    layout.addWidget(QPushButton("打开"))
    layout.addWidget(QPushButton("保存"))
    layout.addWidget(QPushButton("退出"))
    
    # 设置组件拉伸比例（让按钮自适应窗口宽度）
    layout.setStretch(0, 1)
    layout.setStretch(1, 1)
    layout.setStretch(2, 1)
    layout.setStretch(3, 1)
    
    window.show()
    sys.exit(app.exec())

# test2()

'''
4.3 网格布局（QGridLayout）：表格形式排列
QGridLayout 将组件按 “行 × 列” 的表格形式排列，适合复杂的界面布局（如登录窗口、数据表格）。

示例：网格布局的登录窗口
'''
def test3():
    from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QMessageBox
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("QGridLayout示例")
    window.resize(300, 200)
    
    # 创建网格布局
    layout = QGridLayout(window)
    layout.setSpacing(15)
    layout.setContentsMargins(30, 30, 30, 30)
    
    # 添加组件（行索引，列索引，跨行数，跨列数）
    layout.addWidget(QLabel("用户名："), 0, 0)
    layout.addWidget(QLineEdit(), 0, 1, 1, 2)  # 第0行第1列，跨2列(其实是输入框的宽度占2列)
    
    layout.addWidget(QLabel("密码："), 1, 0)
    layout.addWidget(QLineEdit(), 1, 1, 1, 2)
    
    # 登录按钮：第2行第1-2列，跨2列
    login_btn = QPushButton("登录")
    login_btn.clicked.connect(lambda: QMessageBox.information(window, "提示", "登录中..."))
    layout.addWidget(login_btn, 2, 1, 1, 2)
    
    window.show()
    sys.exit(app.exec())

# test3()

'''
4.4 布局嵌套：实现复杂界面
实际开发中，常将多种布局嵌套使用，实现更灵活的界面布局。

示例：嵌套布局的综合示例
'''
def test4():
    from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QGridLayout,QLineEdit
    from PyQt6.QtCore import Qt
    import sys
    
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("布局嵌套示例")
    window.resize(400, 300)
    
    # 主布局：垂直布局
    main_layout = QVBoxLayout(window)
    
    # 顶部区域：水平布局（标题+按钮）
    top_layout = QHBoxLayout()
    top_layout.addWidget(QLabel("复杂界面布局示例"), alignment=Qt.AlignmentFlag.AlignLeft)
    top_layout.addWidget(QPushButton("设置"), alignment=Qt.AlignmentFlag.AlignRight)
    main_layout.addLayout(top_layout)
    
    # 中间区域：网格布局（表单）
    grid_layout = QGridLayout()
    grid_layout.addWidget(QLabel("姓名："), 0, 0)
    grid_layout.addWidget(QLineEdit(), 0, 1)
    grid_layout.addWidget(QLabel("年龄："), 1, 0)
    grid_layout.addWidget(QLineEdit(), 1, 1)
    main_layout.addLayout(grid_layout)
    
    # 底部区域：水平布局（功能按钮）
    bottom_layout = QHBoxLayout()
    bottom_layout.addWidget(QPushButton("确定"))
    bottom_layout.addWidget(QPushButton("取消"))
    main_layout.addLayout(bottom_layout)
    main_layout.setAlignment(bottom_layout, Qt.AlignmentFlag.AlignCenter)
    
    window.show()
    sys.exit(app.exec())

test4()