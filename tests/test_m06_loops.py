import unittest
from modules.m06_loops import sum_with_for, sum_with_while, find_first_even, skip_negatives


class M06Loop(unittest.TestCase):
    def test_sum_with_for(self):

        """
        测试 sum_with_for 函数的正确性

        Args:
            self: 测试类实例

        验证 sum_with_for 函数在以下情况下的输出:
        1. 输入正整数时的求和结果
        2. 输入0时的边界情况
        """
        self.assertEqual(sum_with_for(5), 15)  # 1+2+3+4+5
        self.assertEqual(sum_with_for(0), 0)

    def test_sum_with_while(self):

        """
        测试 sum_with_while 函数的正确性

        Args:
            self: 测试类实例

        测试用例:
            - 验证 sum_with_while(5) 返回 15
            - 验证 sum_with_while(0) 返回 0
        """
        self.assertEqual(sum_with_while(5), 15)
        self.assertEqual(sum_with_while(0), 0)

    def test_find_first_even(self):

        """
        测试 find_first_even 函数的正确性

        验证以下场景：
        1. 列表中包含偶数时返回第一个偶数
        2. 列表中不包含偶数时返回 None
        """
        self.assertEqual(find_first_even([1, 3, 5, 8, 9]), 8)
        self.assertIsNone(find_first_even([1, 3, 5]))

    def test_skip_negatives(self):
        """
        测试 skip_negatives 函数过滤负数的功能

        验证函数能够:
        1. 正确过滤掉输入列表中的所有负数
        2. 当输入全为负数时返回空列表
        3. 保留所有非负数的元素
        """
        self.assertEqual(skip_negatives([1, -2, 3, -4, 5]), [1, 3, 5])
        self.assertEqual(skip_negatives([-1, -2, -3]), [])


if __name__ == '__main__':
    unittest.main()
