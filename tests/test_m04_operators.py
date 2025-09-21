import unittest
from modules.m04_operators import arithmetic_operators, comparison_operators, logical_operators

'''
1. 运算符分为：  
    算术运算符：+，-，  *，/，//，%  
    比较运算符：>，<，>=，<=，==，!=  
    逻辑运算符：and，or，not  
2. 将运算符与运算封装到字典中，返回字典；
3. 从字典中，取得运算方式，与运算结果，进行断言； 如：
    arithmetic_operators(9,2)["+"]=13
    comparison_operators(9,2)[">"]=True
    logical_operators(True,True)["&&"]=True
    


'''

class Mo4Operators(unittest.TestCase):
    def test_arithmetic_operators(self):
        """
               测试算术运算符函数的正确性

               该测试方法验证 arithmetic_operators 函数是否能正确执行各种算术运算，
               包括加法、减法、乘法、除法、整除、取模和幂运算。

               测试使用参数 9 和 2 进行运算，验证返回字典中各运算符对应的结果值。
               """
        # 调用算术运算符函数，传入操作数9和2
        result=arithmetic_operators(9,2)
        self.assertEqual(result["+"], 11)
        self.assertEqual(result["-"], 7)
        self.assertEqual(result["*"], 18)
        self.assertEqual(result["/"], 4.5)
        self.assertEqual(result["//"], 4)
        self.assertEqual(result["%"], 1)
        self.assertEqual(result["**"], 81)

    def test_arithmetic_operators_divide_by_zero(self):
        """
                测试算术运算符在除零情况下的处理

                该函数测试当除数为0时，arithmetic_operators函数是否能正确处理除法、整除和取模运算，
                验证这些运算的结果是否为None以避免除零错误。

                参数:
                    无

                返回值:
                    无
                """
        # 调用算术运算符函数，传入被除数9和除数0
        result=arithmetic_operators(9,0)
        self.assertIsNone(result["/"])
        self.assertIsNone(result["//"])
        self.assertIsNone(result["%"])

    def test_comparison_operators(self):
        """
        测试comparison_operators函数的比较运算符功能
        该函数验证两个数值之间各种比较运算符的正确性

        参数:
            无参数

        返回值:
            无返回值
        """
        # 测试comparison_operators函数，传入参数9和2进行比较运算
        result = comparison_operators(9, 2)

        # 验证各种比较运算符的结果是否正确
        self.assertEqual(result[">"], True)
        self.assertEqual(result["<"], False)
        self.assertEqual(result[">="], True)
        self.assertEqual(result["<="], False)
        self.assertEqual(result["=="], False)
        self.assertEqual(result["!="], True)
        self.assertEqual(result["<>"], True)

    def test_logical_operators(self):

        """
        测试 logical_operators 函数的逻辑运算符功能

        验证逻辑运算符(与、或、非)的正确性：
        1. 测试与运算(&&)结果
        2. 测试或运算(||)结果
        3. 测试第一个操作数的非运算结果
        4. 测试第二个操作数的非运算结果
        """
        result = logical_operators(True, False)
        self.assertEqual(result["&&"], False)
        self.assertEqual(result["||"], True)
        self.assertEqual(result["not_first"], False)
        self.assertEqual(result["not_second"], True)

    def test_logical_operators_with_none(self):

        """
        测试 logical_operators 函数处理 None 值的情况

        测试用例包括：
        1. 传入两个 None 参数时是否抛出 TypeError
        2. 传入单个 True 参数时 'not' 运算的正确性
        3. 传入单个 None 参数时是否抛出 TypeError
        """
        with self.assertRaises(TypeError):
            logical_operators(None, None)
        self.assertEqual(logical_operators(True)["not"], False)
        with self.assertRaises(TypeError):
            logical_operators(None)


if __name__ == '__main__':
    unittest.main()
