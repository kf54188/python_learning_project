import unittest
from modules.m06_loops import sum_with_for, sum_with_while, find_first_even, skip_negatives, break_program


class M06Loop(unittest.TestCase):
    def test_sum_with_for(self):

        """
       使用for循环计算1到n的整数之和

        验证 sum_with_for 函数在以下情况下的输出:
        1. 输入正整数时的求和结果
        2. 输入0时的边界情况
        """
        self.assertEqual(sum_with_for(5), 15)  # 1+2+3+4+5
        self.assertEqual(sum_with_for(0), 0)

    def test_sum_with_while(self):

        """
        使用while循环计算1到n的整数之和

        测试用例:
            - 验证 sum_with_while(5) 返回 15
            - 验证 sum_with_while(0) 返回 0
        """
        self.assertEqual(sum_with_while(5), 15)
        self.assertEqual(sum_with_while(0), 0)

    def test_find_first_even(self):

        """
        使用while循环在列表中查找第一次出现的偶数

        验证以下场景：
        1. 列表中包含偶数时返回第一个偶数
        2. 列表中不包含偶数时返回 None
        """
        self.assertEqual(find_first_even([1, 3, 5, 8, 9]), 8)
        self.assertIsNone(find_first_even([1, 3, 5]))

    def test_skip_negatives(self):
        """
        使用continue语句过滤列表中的负数

        验证函数能够:
        1. 正确过滤掉输入列表中的所有负数
        2. 当输入全为负数时返回空列表
        """
        self.assertEqual(skip_negatives([1, -2, 3, -4, 5]), [1, 3, 5])
        self.assertEqual(skip_negatives([-1, -2, -3]), [])

    def test_break_program(self) :
        '''
        在创建列表时，当添加到5时使用break语句跳出循环
        '''
        self.assertEqual(break_program(), [0,1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
