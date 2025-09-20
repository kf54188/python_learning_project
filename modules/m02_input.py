def ask_name():
    """
    提示用户输入姓名并返回输入结果

    Returns:
        str: 用户输入的名字
    """
    name = input("请输入你的名字：")
    return name


def collect_user_data():
    """
    收集用户输入的个人信息并格式化为字符串

    Args:
        无参数，通过标准输入获取用户数据

    Returns:
        str: 格式化后的用户信息字符串，格式为"名字, 年龄岁, 来自: 城市"

    Raises:
        无显式抛出异常，但会在用户输入无效年龄时返回部分信息
    """
    name = input("请输入你的名字：")
    age_str = input("请输入你的年龄：")
    city = input("请输入所在城市：")

    i = 0
    while i<=3:
        try:
            age = int(age_str)
            break
        except ValueError:
            if i == 3:
                print("年龄必须是数字, 傻子都知道，不和你玩了。拜拜")
                return f"{name}, {age_str}岁, 来自: {city}"
            print("年龄必须是数字")
            age_str = input("请输入你的年龄,年龄必须是数字：")
            # raise ValueError("年龄必须是数字")

        i += 1

    return f"{name}, {age}岁, 来自: {city}"

if __name__ == "__main__":
    # print(ask_name())
    print(collect_user_data())