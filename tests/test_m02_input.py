import sys
import unittest
from io import StringIO
from modules.m02_input import ask_name, collect_user_data


class M02Input(unittest.TestCase):
    '''
    1. 用StringIO 捕获 input()输入;
    2. StringIO 中的内容必须包含换行符 \n，因为 input() 会读取直到换行。
    3. 替换 sys.stdin 后要记得恢复原始值，否则后续代码可能无法正常读取输入

    '''

    def test_user_input(self):
        """
        测试用户输入功能，验证ask_name()函数是否能正确获取并返回用户输入

        测试步骤：
        1. 使用StringIO模拟用户输入"张三"
        2. 调用ask_name()获取输入结果
        3. 断言返回结果与预期值"张三"相等

        Args:
            无

        Returns:
            无

        Raises:
            AssertionError: 如果返回结果与预期值不符
        """
        fake_input = StringIO("张三\n")
        sys.stdin = fake_input
        result = ask_name()

        sys.stdin=sys.__stdin__

        expected= "张三"
        self.assertEqual(result, expected)  # add assertion here

    def test_collect_user_data(self):
        """
                测试collect_user_data函数的功能

                该测试函数用于验证collect_user_data函数能否正确收集用户输入的姓名、年龄和城市信息，
                并返回格式化的字符串。

                测试流程：
                1. 模拟用户输入"张三"、"18"、"上海"
                2. 调用collect_user_data函数收集数据
                3. 验证返回结果是否符合预期格式
        """

        # 创建模拟输入流，包含姓名、年龄、城市三个输入值
        fake_input= StringIO("张三\n18\n上海\n")
        sys.stdin=fake_input
        result = collect_user_data()

        sys.stdin=sys.__stdin__

        expected= "张三, 18岁, 来自: 上海"
        self.assertEqual(result, expected)

    def test_collect_user_data_mult_line(self):
        """
                测试collect_user_data函数处理多行用户输入的情况

                该测试用例模拟用户输入多行数据，验证函数能够正确收集和格式化用户信息
                包括姓名、年龄和地址等字段

                参数:
                    无

                返回值:
                    无
                """
        # 模拟用户输入多行数据，包括姓名、年龄、地址等信息
        fake_input = StringIO("张三\ndd\n上海\ndd\n\dd\ndd\n")
        sys.stdin = fake_input
        result = collect_user_data()

        sys.stdin = sys.__stdin__

        expected = "张三, dd岁, 来自: 上海"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
