import unittest
from modules.m08_collections import list_operations

class M08Collections(unittest.TestCase):
    def test_list_operations(self):
        # 定义list
        li =[1,"a",True,3.14,(1,2)]
        li =[]
        li.append(1) # 添加整形
        li.append("a") # 添加字符串
        li.append(True) # 添加布尔
        li.append(3.14) # 添加浮点型
        li.append((1,2)) # 添加元组
        li.append([1,2]) # 添加列表
        li.append({1,2}) # 添加集合
        li.append({"a":1,"b":2,"c":3}) # 添加字典

        self.assertEqual(1 in li, True)  # 查找
        self.assertEqual(li[1],"a")  # 索引
        self.assertEqual(len(li), 8)  # 长度
        self.assertEqual(li.pop(2), True) # 弹出指定位置的元素
        self.assertEqual(len(li), 7) # 弹出后长度-1
        self.assertEqual(li.pop(), {"a":1,"b":2,"c":3}) # 弹出最后一个元素
        self.assertEqual(len(li), 6) # 弹出后长度-1




if __name__ == '__main__':
    unittest.main()
