import sys
import unittest
from io import StringIO
from modules.m01_output import welcome_message, welcome_message_with_args  # 引用函数

'''
1. 要测试m01_output中的代码，必须从m01_output中导入welcome_message函数；
  - 学习要点：模块，函数，导入
  - 在导入时，利用编程软件的功能，生成或创建模块或函数；
2. 基本操作是：测试代码捕获由业务代码输出到内存中的文字，比较与预期是否一致
    - 学习要点：照抄测试用例中捕获文字的方法；
    - 文本输入/输出的实现使用内存中的缓冲区StringIO；
'''


class M01Output(unittest.TestCase):
    def test_welcome_message(self):

        """
        测试 welcome_message 函数的输出内容是否符合预期

        验证标准输出中是否包含"欢迎来到 Python 学习项目"字符串
        通过重定向标准输出到内存缓冲区进行捕获和断言
        """
        captured_output = StringIO()  # 创建一个内存中的缓冲区
        sys.stdout = captured_output  # 将标准输出重定向到内存中的缓冲区
        welcome_message() #被测试的业务逻辑，内容是: 输出一段文字：“欢迎来到 Python 学习项目”，到控制台；
        sys.stdout=sys.__stdout__ # 恢复标准输出
        result=captured_output.getvalue()
        self.assertIn("欢迎来到 Python 学习项目", result) # 验证文字是否包含在缓冲区中

    def test_welcome_message_with_args(self):
        """
        测试 welcome_message_with_args 函数的输出是否包含所有传入的参数

        Args:
            self: 测试类实例

        验证标准:
            - 输出结果应包含第一个参数"欢迎来到 Python"
            - 输出结果应包含第二个参数"学习项目"
            - 输出结果应包含第三个参数"Python 3.7.3"
        """
        captured_output = StringIO()
        sys.stdout = captured_output
        welcome_message_with_args("欢迎来到 Python", "学习项目", "Python 3.7.3") ## 三段
        sys.stdout=sys.__stdout__
        result = captured_output.getvalue()
        self.assertIn("欢迎来到 Python", result)
        self.assertIn("学习项目", result)
        self.assertIn("Python 3.7.3", result)
        # print("结果是： ",captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
