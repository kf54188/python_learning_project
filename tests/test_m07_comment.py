import unittest
from modules.m07_comments import calculate_rectangle_area,is_valid_name


class MyTestCase(unittest.TestCase):
    '''
    PEP8 是 Python 官方的编码风格指南，全称是 Python Enhancement Proposal 8，
    旨在统一 Python 代码的书写风格，提高代码的可读性和一致性。
    详细请参考：https://www.python.org/dev/peps/pep-0008/
    '''


    def test_calculate_rectangle_area(self):
        '''
        注释：
            计算矩形的面积
        '''
        result = calculate_rectangle_area(3, 4)
        self.assertEqual(result, 12)  # add assertion here, False)  # add assertion here

    def test_is_valid_name(self):
        '''
        利用is_valid_name函数验证变量/函数名、类名、常量名的命名规则
        不匹配变量/函数名：
            - UserName（含大写）
            - user Name（含空格）
            1st_value（数字开头）

        '''
        self.assertEqual(is_valid_name("user_name")["变量与函数名"] ,True)
        self.assertEqual(is_valid_name("user_name_1")["变量与函数名"] ,True)
        self.assertEqual(is_valid_name("userName")["变量与函数名"] ,False)
        self.assertEqual(is_valid_name("user name")["变量与函数名"] ,False)
        self.assertEqual(is_valid_name("1th_user")["变量与函数名"] ,False)

        '''
        不匹配类名：
            - userProfile（首字母小写）
            - user_profile（蛇形命名）
            - User Profile（含空格）
        '''
        self.assertEqual(is_valid_name("UserName")["类名"],True)
        self.assertEqual(is_valid_name("User_Name")["类名"],True)
        self.assertEqual(is_valid_name("user_name")["类名"],False)
        self.assertEqual(is_valid_name("userName")["类名"],False)
        self.assertEqual(is_valid_name("user Name")["类名"],False)
        '''
        不匹配常量名：
            - MaxSize（含小写）
            - max_size（蛇形命名）
            - MAX SIZE（含空格）
        '''
        self.assertEqual(is_valid_name("USERNAME")["常量"],True)
        self.assertEqual(is_valid_name("USER_NAME")["常量"],True)
        self.assertEqual(is_valid_name("UserName")["常量"],False)
        self.assertEqual(is_valid_name("user_name")["常量"],False)

if __name__ == '__main__':
    unittest.main()
