import unittest
from modules.m03_format import std_format, f_format, str_format,str_newline, make_tab_string, make_quote_string, make_backslash_string, replace_newline_with_space,escape_to_visible


class M04Format(unittest.TestCase):
    def test_std_format(self):

        """
        将若干段文字按'%'方式合并后，输出到控制台，
        四段文字：张三，18，上海，3.5678
        输出：姓名: 张三, 年龄: 000018, 城市：上海, 有3.57元
        """
        result = std_format()
        expected = "姓名: 张三, 年龄: 000018, 城市：上海, 有3.57元"
        self.assertEqual(expected, result)  # add assertion here

    def test_f_format(self):

        """
        将若干段文字按'f'方式合并后，输出到控制台，
        四段文字：张三，18，上海，3.5678
        输出：姓名: 张三, 年龄: 000018, 城市：上海, 有3.57元
        """
        result = f_format()
        age = 18
        age_str=str(age).zfill(6) # 将 age 转换为 6 位长度的字符串，不足部分用 0 填充
        expected = "姓名: 张三, 年龄: " + age_str + ", 城市：上海, 有3.57元"
        self.assertEqual(expected, result)  # ad  # add assertion here


    def test_str_format(self):
        """
        将若干段文字按'.format()'方式合并后，输出到控制台，
        四段文字：张三，18，上海，3.5678
        输出：姓名: 张三, 年龄: 000018, 城市：上海, 有3.57元
        """
        result = str_format()
        expected = "姓名: 张三, 年龄: 000018, 城市：上海, 有3.57元"
        self.assertEqual(expected,result)  # ad  # add assertion here

    def test_newline_str(self):
        '''
        业务需求：编辑包含有换行符的字符串，返回给调用者
        输入：姓名: 张三, 年龄: 18, 城市：上海, 有3.57元
        输出：姓名: 张三,
            年龄: 000018,
            城市：上海,
            有3.57元

        “\n”:换行
        “\t”:制表符
        "\"":双引号
        "\'":单引号
        "\\":反斜杠
        "\\n":转义字符
        "r""“:原始字符串，不进行转义
        '''
        result = str_newline()
        expected = "姓名: 张三,\n年龄: 18,\n城市：上海,\n有3.57元"
        self.assertEqual(expected,result)

    def test_make_tab_string(self):
        '''
        业务需求：编辑包含有制表符的字符串，返回给调用者
        输入：姓名\t年龄\t城市\t3.57元
             张三\t18\t上海\t3.57元
        输出：姓名\t年龄\t城市\t3.57元\n张三\t18\t上海\t3.57元
        '''
        result = make_tab_string()
        expected = "姓名\t年龄\t城市\t3.57元\n张三\t18\t上海\t3.57元"
        self.assertEqual(expected,result)

    def test_make_quote_string(self):
        """
           返回包含引号的字符串
        """
        result = make_quote_string()
        expected= "She said: \"Hello\" and left."
        self.assertEqual(expected,result)

    def test_make_backslash_string(self):
        """
        返回包含反斜杠的字符串
        """
        result = make_backslash_string()
        expected = "C:\\Users\\Administrator\\Desktop\\test.txt"
        self.assertEqual(expected,result)

    def test_replace_newline_with_space(self):
        """
        将字符串中的换行符替换为空格
        """
        result = replace_newline_with_space("Hello\nWorld")
        expected = "Hello World"
        self.assertEqual(expected,result)

    def test_escape_to_visible(self):
        """
        将字符串中的特殊字符转义为可见字符
        """
        input = "\nA\tB\tC\nHello\tWorld\td:\\temp\n"
        print(input)
        result = escape_to_visible(input)
        expected = "\\nA\\tB\\tC\\nHello\\tWorld\\td:\\\\temp\\n"
        print(result)
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()
