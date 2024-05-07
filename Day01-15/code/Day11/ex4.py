"""
引发异常和异常栈

Version: 0.1
Author: Maxwell
Date: 2024-05-07
"""


def f1():
    raise AssertionError('发生异常')


def f2():
    f1()


def f3():
    f2()


f3()