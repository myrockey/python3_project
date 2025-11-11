#!/usr/bin/python3

from io import StringIO
import unittest

# 单元测试中的使用
# 在单元测试中，StringIO 可以用于模拟文件对象，方便我们测试代码的输入输出。
def process_input(input_data):
    return input_data.upper()

class TestProcessInput(unittest.TestCase):
    def test_process_input(self):
        input_data = 'hello'
        excepted_output = 'HELLO'

        # 使用StringIO 模拟输入
        input_stream = StringIO(input_data)
        result = process_input(input_stream.read())

        self.assertEqual(result,excepted_output)

if __name__ == '__main__':
    unittest.main()