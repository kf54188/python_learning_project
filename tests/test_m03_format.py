import unittest
from modules.m03_format import std_format, f_format, str_format


class M04Format(unittest.TestCase):
    def test_std_format(self):
        result =std_format()
        expected="姓名: 张三, 年龄: 000018, 城市：上海, 有3.57元"
        self.assertEqual(expected, result)  # add assertion here



    def test_f_format(self):
        result = f_format()
        age=18;
        age_str=str(age).zfill(6)
        expected = "姓名: 张三, 年龄: " + age_str + ", 城市：上海, 有3.57元"
        self.assertEqual(expected, result)  # ad  # add assertion here


    def test_str_format(self):
        result = str_format()
        expected = "姓名: 张三, 年龄: 000018, 城市：上海, 有3.57元"
        self.assertEqual(expected,result)  # ad  # add assertion here


if __name__ == '__main__':
    unittest.main()
