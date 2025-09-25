# PEP8 编码风格指南

PEP8 是 Python 官方的编码风格指南，全称是 Python Enhancement Proposal 8，
旨在统一 Python 代码的书写风格，提高代码的可读性和一致性。下面是 PEP8 的核心内容分类整理：

## 🧠 命名规范（Naming Conventions）
|类型|	推荐风格| 	示例                         |
|----| -------- |-----------------------------|
|变量名 / 函数名|	小写字母 + 下划线	| user_name, get_data()       |
|常量名|	全大写 + 下划线| 	MAX_SIZE, DEFAULT_COLOR    |
|类名|	首字母大写驼峰式| 	UserProfile, DataLoader    |
|模块/ 包名| 	全小写，可加下划线| 	utils, data_loader         |
|私有变量|	前缀一个下划线	| _hidden_value               |
|特殊方法|	双下划线包裹| \_\_init\_\_, \_\_str\_\_ |

## 📏 缩进与空格（Indentation & Whitespace）
- 使用 4 个空格 作为缩进（不要用 Tab）；

- 运算符两边加空格：a = b + c；

- 函数参数逗号后加空格：func(a, b)；

- 不要在括号内侧加空格：list[1] 而不是 list[ 1 ]；

- 不要在函数定义和调用的 = 两边加空格（关键字参数除外）：func(x=1) ✅


## 📄 注释规范（Comments）
- 单行注释用 #，后面加一个空格；

- 多行注释建议使用文档字符串 """docstring"""；

- 文档字符串应出现在函数、类、模块的第一行；

- 注释应简洁明了，避免重复代码逻辑。

## 📚 代码结构（Code Layout）
- 每个模块建议不超过 400 行；

- 每个函数建议不超过 20 行；

- 函数之间空两行，类中方法之间空一行；

- 导入语句分三组：标准库、第三方库、自定义模块，并用空行分隔。

## 🔍 其他建议
- 避免使用 from module import *；

- 使用 is / is not 比较 None；

- 布尔值判断推荐：if value: 而不是 if value == True:；

- 字符串拼接推荐使用 join() 或 f-string；

- 使用异常处理时，尽量具体捕获异常类型。

## 📘 官方资源
PEP8 原文地址：[PEP8 官方文档](https://peps.python.org/pep-0008/) 你也可以使用工具自动检查代码风格，比如：

- flake8：检查语法和风格；

- black：自动格式化代码；

- pylint：代码质量评分和建议。