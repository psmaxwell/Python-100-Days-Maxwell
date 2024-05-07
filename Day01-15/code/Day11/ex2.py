"""
异常机制 - 处理程序在运行时可能发生的状态 2

Version: 0.1
Author: Maxwell
Date: 2024-05-07
"""
input_again = True
while input_again:
    try:
        a = int(input('a = '))
        b = int(input('b = '))
        print('%d / %d = %f' % (a, b, a / b))
        input_again = False
    except (ValueError, ZeroDivisionError) as msg:
        print(msg)

