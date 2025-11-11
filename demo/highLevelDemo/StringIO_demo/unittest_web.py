import unittest
from playwright.sync_api import sync_playwright

class TestWeb(unittest.TestCase):
    def setUp(self):
        self.p = sync_playwright().start()
        # ↓↓↓ 关键：headless=False 才能看见窗口(浏览器打开窗口)，默认是 headless=True，不显示浏览器窗口
        self.browser = self.p.chromium.launch(headless=False)

    def tearDown(self):
        self.browser.close() #  关闭，否则进程会残留
        self.p.stop()
        # pass

    def test_title(self):
        page = self.browser.new_page()
        page.goto("https://www.baidu.com")
        self.assertEqual(page.title(), "百度一下，你就知道")

if __name__ == '__main__':
    unittest.main()

'''
这段代码把 unittest 和 playwright 结合起来，让“打开真浏览器访问页面”这件事变成了单元测试用例。
下面按执行顺序逐行解释每个方法是谁、什么时候被调用、干了什么。
1. import unittest
引入 Python 标准单元测试框架，提供 TestCase 基类 和 测试发现、断言、结果收集 等能力。
2. from playwright.sync_api import sync_playwright
从 playwright 库里拿同步入口函数 sync_playwright()，用来启动/关闭浏览器实例。
3. class TestWeb(unittest.TestCase):
继承 unittest.TestCase，告诉框架：
“这里面试所有以 test_ 开头的方法都是一条测试用例”。
4. setUp(self) —— 每条测试开始前自动运行
表格
复制
代码	作用
self.p = sync_playwright().start()	启动 playwright 管理器（浏览器驱动进程）
self.browser = self.p.chromium.launch()	打开一个 Chromium 浏览器实例（默认 headless=True，这里可见窗口）
注：unittest 约定：每条 test_* 方法运行前都会先跑 setUp()，保证测试之间相互隔离。
5. tearDown(self) —— 每条测试结束后自动运行
表格
复制
代码	作用
self.browser.close()	关闭浏览器
self.p.stop()	关掉 playwright 管理器，释放资源
即使测试失败/抛异常，tearDown() 仍会被调用，确保不会留下僵尸进程。
6. test_title(self) —— 真正的测试用例
表格
复制
代码	作用
page = self.browser.new_page()	新建一个空白标签页
page.goto("https://www.baidu.com")	让标签页跳转到百度首页
self.assertEqual(page.title(), "百度一下，你就知道")	断言页面标题必须是期望文字；
若不相等，unittest 会把这条测试标记为 失败
7. if __name__ == '__main__': unittest.main()
当脚本被直接运行时，启动 unittest 的测试主循环：
自动发现当前文件中所有 test_* 方法 → 依次执行（先 setUp → 测试 → tearDown）→ 输出结果摘要。
执行流程时间线（单条用例）
复制
unittest.main()
 └─ 实例化 TestWeb
 └─ 调用 setUp()        → 启动浏览器
 └─ 调用 test_title()   → 打开百度并断言标题
 └─ 调用 tearDown()     → 关闭浏览器
输出：OK / FAILED / ERROR
一句话总结
setUp/tearDown 是 unittest 提供的 「前置/后置」钩子，保证每条测试都有独立的浏览器环境；
test_title 里用 playwright 的 API 完成真实浏览器操作，再用 unittest 的断言判断结果是否达标。
'''