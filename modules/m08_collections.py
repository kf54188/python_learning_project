


def list_intersection(list1: list[int], list2: list[int]) -> list[int]:
    """
    返回两个列表的交集（去重）
    """
    return list(set(list1) & set(list2))


def list_union(list1: list[int], list2: list[int]) -> list[int]:
    """
    返回两个列表的并集（去重）
    """
    return list(set(list1) | set(list2))


def list_difference(list1: list[int], list2: list[int]) -> list[int]:
    """
    返回 list1 中有而 list2 中没有的元素（差集）
    """
    return list(set(list1) - set(list2))


def set_intersection(set1: set[int], set2: set[int]) -> set[int]:
    """
    返回两个集合的交集
    """
    return set1 & set2


def set_union(set1: set[int], set2: set[int]) -> set[int]:
    """
    返回两个集合的并集
    """
    return set1 | set2


def set_difference(set1: set[int], set2: set[int]) -> set[int]:
    """
    返回 set1 中有而 set2 中没有的元素（差集）
    """
    return set1 - set2


def list_operations():
    return None