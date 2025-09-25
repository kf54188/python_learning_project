
import re

# 单选注释：计算矩形的面积
def calculate_rectangle_area(width: float, height: float) -> float:
    return width * height


import re

# 预编译正则表达式以提高性能
_VARIABLE_FUNC_PATTERN = re.compile(r'^[a-z_][a-z0-9_]*$')
_CONSTANT_PATTERN = re.compile(r'^[A-Z][A-Z0-9_]*$')
_CLASS_PATTERN = re.compile(r'^[A-Z][a-zA-Z0-9_]*$')

# 初学者不用关心函数的内容，只用它来在测试中进行测试
def is_valid_name(name: str) -> dict:
    # 添加输入类型检查
    if not isinstance(name, str):
        raise TypeError("name must be a string")

    return {
        "变量与函数名": bool(_VARIABLE_FUNC_PATTERN.fullmatch(name)),
        "常量": bool(_CONSTANT_PATTERN.fullmatch(name)),
        "类名": bool(_CLASS_PATTERN.fullmatch(name)),
    }
