import unittest
from modules.m03_format import std_format, f_format, str_format


class M04Format(unittest.TestCase):
    def test_std_format(self):

        """
        测试 std_format 函数的输出格式是否符合预期

        Args:
            无

        Returns:
            无

        Raises:
            AssertionError: 如果 std_format() 的输出与预期字符串不匹配
        """
        result = std_format()
        expected = "姓名: 张三, 年龄: 000018, 城市：上海, 有3.57元"
        self.assertEqual(expected, result)  # add assertion here

    def test_f_format(self):

        """
        测试 f_format 函数的输出格式是否符合预期

        验证函数返回的字符串是否包含正确的姓名、年龄（6位数字填充）、城市和金额格式

        Args:
            无

        Returns:
            无

        Raises:
            AssertionError: 如果实际结果与预期结果不匹配
        """
        result = f_format()
        age = 18;
        age_str=str(age).zfill(6)
        expected = "姓名: 张三, 年龄: " + age_str + ", 城市：上海, 有3.57元"
        self.assertEqual(expected, result)  # ad  # add assertion here


    def test_str_format(self):
        """
        测试 str_format 函数的输出格式是否符合预期

        Args:
            无

        Returns:
            无

        Raises:
            AssertionError: 如果 str_format() 的输出与预期字符串不匹配
        """
        result = str_format()
        expected = "姓名: 张三, 年龄: 000018, 城市：上海, 有3.57元"
        self.assertEqual(expected,result)  # ad  # add assertion here


if __name__ == '__main__':
    unittest.main()
