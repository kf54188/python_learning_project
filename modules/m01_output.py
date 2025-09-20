'''
   定义一个函数，让函数拿出一段文字。输出文字的方法是：print("......");
'''


def welcome_message():
    """
       打印欢迎信息到控制台

       无参数

       无返回值
       """
    # print("欢迎来到 Python")
    print("欢迎来到 Python 学习项目")

'''
定义了一个名为welcome_message_with_args的函数，
它接受任意数量的位置参数（通过*message实现可变参数）。
函数的功能是将所有传入的参数作为一个元组打印出来。
'''
def welcome_message_with_args(*message):
    """
        打印传入的消息参数

        参数:
            *message: 可变长度参数，接收任意数量的位置参数，将它们作为元组传递

        返回值:
            无返回值

        说明:
            该函数接收任意数量的参数，并将它们作为一个元组直接打印输出
        """
    print(message)