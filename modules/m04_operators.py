def comparison_operators(num1, num2):
    """
    比较两个数字的所有常见比较运算符结果

    Args:
        num1 (int|float): 第一个比较数字
        num2 (int|float): 第二个比较数字

    Returns:
        dict: 包含各种比较运算符结果的字典，键为运算符字符串，值为比较结果(bool)

    Raises:
        TypeError: 当输入参数不是数字类型时抛出
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("num1 和 num2 参数必须是数字")
    return {
        ">": num1 > num2,
        "<": num1 < num2,
        ">=": num1 >= num2,
        "<=": num1 <= num2,
        "==": num1 == num2,
        "!=": num1 != num2,
        "<>": num1 != num2,
    }


def arithmetic_operators(num1, num2)->dict:
    """
    对两个数字执行基本算术运算并返回结果字典。

    Args:
        num1 (int|float): 第一个操作数
        num2 (int|float): 第二个操作数

    Returns:
        dict: 包含各种算术运算结果的字典，键为运算符符号，值为运算结果。
              除法相关运算在除数为0时返回None。

    Raises:
        TypeError: 当输入参数不是数字类型时抛出
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("num1 和 num2 参数必须是数字")
    return {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2 if num2 != 0 else None,
        "//": num1 // num2 if num2 != 0 else None,
        "%": num1 % num2 if num2 != 0 else None,
        "**": num1 ** num2
    }


def logical_operators(num1, num2=None):
    """
    对布尔值执行逻辑运算并返回结果

    Args:
        num1 (bool): 第一个布尔值参数
        num2 (bool, optional): 第二个布尔值参数，默认为None

    Returns:
        dict: 包含不同逻辑运算结果的字典，键为运算类型，值为运算结果
            - 当提供两个参数时返回:
                "&&": 逻辑与结果
                "||": 逻辑或结果
                "not_first": 第一个参数的逻辑非
                "not_second": 第二个参数的逻辑非
            - 当只提供一个参数时返回:
                "not": 参数的逻辑非
                "not_first": 参数的逻辑非
                "not_second": 参数的逻辑非

    Raises:
        TypeError: 当参数不是布尔值时抛出
    """
    if isinstance(num1, bool) and isinstance(num2, bool):
        return {
            "&&": num1 and num2,
            "||": num1 or num2,
            "not_first": not num1,
            "not_second": not num2,
        }
    elif isinstance(num1, bool) and num2 is None:
        return {
            "not": not num1,
            "not_first": not num1,
            "not_second": not num1,
        }
    else :
        raise TypeError("num1 和 num2 参数必须是布尔值")
