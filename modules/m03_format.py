'''
    .2f 保留两位小数,但是四舍五入
'''


def std_format() -> str:
    """
    返回一个标准格式的字符串示例

    Returns:
        str: 格式化后的字符串，包含姓名、年龄、城市和金额信息
        格式为："姓名: 张三, 年龄: 000018, 城市：上海, 有3.57元"
    """
    return "姓名: %s, 年龄: %06d, 城市：%s, 有%.2f元" % ("张三", 18, "上海", 3.5678)


def f_format()->str:

    name="张三"
    age=18
    city="上海"
    money=3.5678
    return f"姓名: {name}, 年龄: {age:06d}, 城市：{city}, 有{money:.2f}元"


def str_format()->str:

    return "姓名: {}, 年龄: {:06d}, 城市：{}, 有{:.2f}元".format("张三", 18, "上海", 3.5678)


if __name__ == '__main__':
    print(std_format())
    print(f_format())
    print(str_format())