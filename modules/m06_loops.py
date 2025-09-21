def sum_with_for(n) -> int:
    """
    用for循环 计算从1到n的整数和

    参数:
        n (int): 正整数，表示求和的上界

    返回值:
        int: 从1到n的整数和
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n 必须是正整数")

    sum = 0
    # 使用循环累加1到n的整数
    for i in range(1,n+1):
        sum += i
    return sum


def sum_with_while(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("n 必须是正整数")
    sum=0
    i=1
    while i <=n:
        sum += i
        i += 1
    return sum


def find_first_even(nums: list) -> int:
    if not isinstance(nums, list):
        raise ValueError("nums 必须是一个列表")
    for i in nums:
        if i % 2 == 0:
            return i
    return None


def skip_negatives(nums: list[int]) -> list[int]:
    if not isinstance(nums, list):
        raise ValueError("nums 必须是一个列表")
    result = []
    for i in nums:
        if i < 0:
            continue
        result.append(i)
    return result