'''
   定义一个函数，让函数输出一段文字。输出文字的方法是：print("......");
'''


def welcome_message():
    """
       打印欢迎信息到控制台
       信息是：欢迎来到 Python 学习项目
    """
    # print("欢迎来到 Python")
    print("欢迎来到 Python 学习项目")

    '''
    定义了一个名为welcome_message_with_args的函数，
    它接受任意数量的位置参数（通过*message实现可变位置参数）。
    函数的功能是将所有传入的参数作为一个元组打印出来。
    '''
def welcome_message_with_args(*message):
    """
        打印输入的多段消息
    """
    print(message)