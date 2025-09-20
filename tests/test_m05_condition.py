import unittest
from modules.m05_condition import evaluate_score

class MyTestCase(unittest.TestCase):
    '''
    评价成绩
    1. 90分以上为优秀:98分以上为优+
    2. 75分以上为良好
    3. 60分以上为及格
    4. 60分以下为不及格
    5. >100 或  <0 为无效成绩
    '''
    def test_evaluate_score(self):
        # 大于90
        self.assertEqual(evaluate_score(90), "优秀")
        self.assertEqual(evaluate_score(97), "优秀")
        # 大于98
        self.assertEqual(evaluate_score(98), "优+")
        self.assertEqual(evaluate_score(100), "优+")
        # 大于75
        self.assertEqual(evaluate_score(75), "良好")
        self.assertEqual(evaluate_score(89), "良好")
        # 大于60
        self.assertEqual(evaluate_score(60), "及格")
        self.assertEqual(evaluate_score(74), "及格")
        # 小于60
        self.assertEqual(evaluate_score(59), "不及格")
        self.assertEqual(evaluate_score(0), "不及格")
        # 大于100 或 <0
        self.assertEqual(evaluate_score(101), "无效分数")
        self.assertEqual(evaluate_score(-1), "无效分数")
        # 非数字
        self.assertEqual(evaluate_score("a"), "无效分数")


if __name__ == '__main__':
    unittest.main()
