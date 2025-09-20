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
        fake_input= StringIO("张三\n18\n上海\n")
        sys.stdin=fake_input
        result = collect_user_data()

        sys.stdin=sys.__stdin__

        expected= "张三, 18岁, 来自: 上海"
        self.assertEqual(result, expected)

    def test_collect_user_data_mult_line(self):
        fake_input = StringIO("张三\ndd\n上海\ndd\n\dd\ndd\n")
        sys.stdin = fake_input
        result = collect_user_data()

        sys.stdin = sys.__stdin__

        expected = "张三, dd岁, 来自: 上海"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
