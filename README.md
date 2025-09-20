# 🧪 Python语法与面向对象编程学习项目（TDD驱动）

本项目旨在通过测试驱动开发（TDD）方式系统学习 Python 的基础语法、高级特性与面向对象编程。每个模块都包含功能代码与测试代码，适合初学者逐步掌握 Python 编程技巧。

## 📌 项目目标

构建一个模块化的 Python 学习项目，涵盖从基础语法到面向对象编程的核心知识点。每个模块都包含功能代码与测试代码，采用测试驱动开发（TDD）方式，帮助你边写边学、边测边练。

## 预备知识
1. 认识Python基础语法中的注释，即：单行上`#`后的内容， 多行中，‘’‘注释’‘’，用前后各3个单引号去包裹不准备运行的内容就是注释
2. 各个单元学习，阅读的顺序为：语句块前的注释，语句块，语句前的注释，语句；
3. 测试驱动开发是由实现测试用例而驱动业务代码的生成。
4. 测试驱动框架搭建后，先使用，后理解；无所谓先有鸡或先有蛋。
5. 测试驱动开发一般步骤为：先写测试用例，边写测试代码，边生成业务代码，测试过，代码成。


## 📦 项目结构

### 骨干项目
```
python_learning_project/ 
├── modules/ # 功能模块 
├── tests/ # 测试模块
└── docs/ # 业务需求文档
```
### 模块结构
```
python_learning_project/
│
├── README.md
├── requirements.txt
│
├── modules/                  # 功能模块
│   ├── m01_output.py
│   ├── m02_input.py
│   ├── m03_format.py
│   ├── m04_operators.py
│   ├── m05_condition.py
│   ├── m06_loops.py
│   ├── m07_comments.py
│   ├── m08_collections.py
│   ├── m09_dict_string.py
│   ├── m10_scope.py
│   ├── m11_lambda_builtin.py
│   ├── m12_unpack_exceptions.py
│   ├── m13_modules_packages/
│   │   ├── __init__.py
│   │   └── tools.py
│   ├── m14_recursion_decorator.py
│   └── oop/
│       ├── base_class.py
│       ├── inheritance.py
│       ├── polymorphism.py
│       ├── magic_methods.py
│       └── __init__.py
│
├── tests/                    # 测试模块
│   ├── test_m01_output.py
│   ├── test_m02_input.py
│   ├── test_m03_format.py
│   ├── test_m04_operators.py
│   ├── test_m05_condition.py
│   ├── test_m06_loops.py
│   ├── test_m08_collections.py
│   ├── test_m09_dict_string.py
│   ├── test_m10_scope.py
│   ├── test_m11_lambda_builtin.py
│   ├── test_m12_unpack_exceptions.py
│   ├── test_m14_recursion_decorator.py
│   ├── test_oop.py
│   └── __init__.py
│
└── docs/
    └── business_requirements.md
```
### 结构的学习要点
1. modules和tests是存放功能代码的目录，即：python的包。
2. 每个.py文件中存放功能代码，即：python的模块。
3. 语法：from 模块 import xxx； 即：从模块中引入方法或类或其他需要的功能；
4. 引入的模块，都是单例的；即：同一个模块，多次导入，只会创建一个实例。
5. 为便于驱动开发，tests包中的每一个模块都对应一个modules中的功能模块；测试代码与功能代码一一对应。
6. 

## 🧱 模块说明与语法点覆盖

|模块编号|模块名称|涉及语法点|
|:-----|:-----|:-----|
|M01|输出与注释|print()、字符串、注释、转义字符|
|M02|输入与变量|input()、变量、类型转换、标识符命名规范|
|M03|字符串格式化|f-string、format()、转义字符|
|M04|运算符练习|算术、比较、逻辑运算符|
|M05|条件判断|if、elif、else、布尔表达式|
|M06|循环语句|for、while、break、continue|
|M07|注释与规范|单行/多行注释、PEP8命名规范|
|M08|列表与集合运算|list、set、集合交集、并集、差集|
|M09|字典与字符串处理|dict操作、字符串转集合、去重|
|M10|函数嵌套与作用域|局部变量、全局变量、nonlocal、嵌套函数|
|M11|匿名函数与内置函数|lambda、map()、filter()、len()、sum()|
|M12|拆包与异常处理|元组/列表拆包、try/except/finally、raise|
|M13|模块与包结构|import、模块划分、包结构、__init__.py|
|M14|递归与装饰器|递归函数、尾递归、函数装饰器 @decorator|
|M15|类定义与实例化|class、__init__()、__del__()|
|M16|封装与继承|私有属性、继承、super()|
|M17|多态与类方法|方法重写、@classmethod、@staticmethod|
|M18|魔术方法与属性|__str__()、__repr__()、__new__()、__len__()、__getitem__()等|


## 🧪 示例：装饰器模块（m14_recursion_decorator.py）
```python
def repeat_twice(func):
    def wrapper(name):
        return f"{func(name)}\n{func(name)}"
    return wrapper

@repeat_twice
def greet(name):
    return f"Hello, {name}!"
```

测试文件：test_m14_recursion_decorator.py
```python
import unittest
from modules.m14_recursion_decorator import greet

class TestDecorator(unittest.TestCase):
    def test_repeat_twice(self):
        result = greet("服")
        self.assertEqual(result, "Hello, 服!\nHello, 服!")
```

## 🚀 快速开始

```bash
git clone https://github.com/kf54188/python_learning_project.git
cd python_learning_project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest tests/
```
