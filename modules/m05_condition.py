

def evaluate_score(score)->str:
    """
    根据分数评估等级

    参数:
        score: 待评估的分数，应为数字类型(int或float)

    返回值:
        str: 评估结果，可能的值包括：
             - "优+"：分数在98-100之间
             - "优秀"：分数在90-97之间
             - "良好"：分数在75-89之间
             - "及格"：分数在60-74之间
             - "不及格"：分数在0-59之间
             - "无效分数"：分数不在0-100范围内或不是数字类型
    """
    # 检查输入参数是否为有效数字类型
    if not isinstance(score, (int, float)):
        return "无效分数"
    # 检查分数是否在有效范围内
    elif score > 100 or score < 0:
        return "无效分数"
    # 评估优秀等级（90分及以上）
    elif score >= 90:
        # 进一步细分优秀等级中的"优+"级别
        if score >= 98:
            return "优+"
        return "优秀"
    # 评估良好等级（75-89分）
    elif score >= 75:
        return "良好"
    # 评估及格等级（60-74分）
    elif score >= 60:
        return "及格"
    # 剩余情况为不及格（0-59分）
    else:
        return "不及格"

