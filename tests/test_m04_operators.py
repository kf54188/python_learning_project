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
        result=arithmetic_operators(9,2)
        self.assertEqual(result["+"], 11)
        self.assertEqual(result["-"], 7)
        self.assertEqual(result["*"], 18)
        self.assertEqual(result["/"], 4.5)
        self.assertEqual(result["//"], 4)
        self.assertEqual(result["%"], 1)
        self.assertEqual(result["**"], 81)

    def test_arithmetic_operators_divide_by_zero(self):
        result=arithmetic_operators(9,0)
        self.assertIsNone(result["/"])
        self.assertIsNone(result["//"])
        self.assertIsNone(result["%"])

    def test_comparison_operators(self):
        result=comparison_operators(9,2)
        self.assertEqual(result[">"], True)
        self.assertEqual(result["<"], False)
        self.assertEqual(result[">="], True)
        self.assertEqual(result["<="], False)
        self.assertEqual(result["=="], False)
        self.assertEqual(result["!="], True)
        self.assertEqual(result["<>"], True)

    def test_logical_operators(self):
        result=logical_operators(True,False)
        self.assertEqual(result["&&"], False)
        self.assertEqual(result["||"], True)
        self.assertEqual(result["not_first"], False)
        self.assertEqual(result["not_second"], True)

    def test_logical_operators_with_none(self):
        with self.assertRaises(TypeError):
            logical_operators(None,None)
        self.assertEqual(logical_operators(True)["not"], False)
        with self.assertRaises(TypeError):
            logical_operators(None)


if __name__ == '__main__':
    unittest.main()
