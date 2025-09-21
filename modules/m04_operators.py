

def arithmetic_operators(num1, num2)->dict:
    """
        对两个数字执行基本算术运算并返回结果字典。
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

def comparison_operators(num1, num2):
    """
    比较两个数字的所有常见比较运算符结果
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



def logical_operators(num1, num2=None):
    """
    对布尔值执行逻辑运算并返回结果
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
