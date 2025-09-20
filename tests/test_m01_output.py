import sys
import unittest
from io import StringIO
from modules.m01_output import welcome_message, welcome_message_with_args  # 引用函数

'''
1. 要测试m01_output中的代码，必须从m01_output中导入welcome_message函数；
  - 学习要点：模块，函数，导入
2. 基本操作是：测试代码捕获由业务代码输出的内存中的文字，比较与预期是否一致
    - 学习要点：照抄测试用例中捕获文字的方法；
    - 文本输入/输出的实现使用内存中的缓冲区StringIO；
'''

class M01Output(unittest.TestCase):
    def test_welcome_message(self):
        captured_output=StringIO() # 创建一个内存中的缓冲区
        sys.stdout=captured_output # 将标准输出重定向到内存中的缓冲区
        welcome_message() #被测试的业务逻辑，内容是: 输出一段文字：“欢迎来到 Python 学习项目”，到控制台；
        sys.stdout=sys.__stdout__ # 恢复标准输出
        result=captured_output.getvalue()
        self.assertIn("欢迎来到 Python 学习项目", result) # 验证文字是否包含在缓冲区中

    def test_welcome_message_with_args(self):
        captured_output=StringIO()
        sys.stdout=captured_output
        welcome_message_with_args("欢迎来到 Python", "学习项目", "Python 3.7.3") ## 三段
        sys.stdout=sys.__stdout__
        result = captured_output.getvalue()
        self.assertIn("欢迎来到 Python", result)
        self.assertIn("学习项目", result)
        self.assertIn("Python 3.7.3", result)
        # print("结果是： ",captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
