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

def str_newline()->str:
    '''
    “\n”:换行
    “\t”:制表符
    "\"":双引号
    "\'":单引号
    "\\":反斜杠
    "\\n":转义字符
    '''
    return "姓名: 张三,\n年龄: 18,\n城市：上海,\n有3.57元"

def make_tab_string() -> str:
    """
    返回包含制表符的字符串
    """
    return "姓名\t年龄\t城市\t3.57元\n张三\t18\t上海\t3.57元"


def make_quote_string() -> str:
    """
    返回包含引号的字符串
    """
    return "She said: \"Hello\" and left."


def make_backslash_string() -> str:
    """
    返回包含反斜杠的字符串
    """
    return "C:\\Users\\Administrator\\Desktop\\test.txt"


def replace_newline_with_space(s: str) -> str:
    """
    将字符串中的换行符替换为空格
    """
    return s.replace("\n", " ")


def escape_to_visible(s: str) -> str:
    """
    将转义字符替换为可见形式：
    - 换行符 -> \\n
    - 制表符 -> \\t
    - 反斜杠 -> \\\\
    """
    return (
        s.replace("\\", "\\\\")
         .replace("\n", "\\n")
         .replace("\t", "\\t")
    )
if __name__ == '__main__':
    print(std_format())
    print(f_format())
    print(str_format())


