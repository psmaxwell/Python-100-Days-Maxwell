"""
写文本文件
将100以内的素数写入到文件中

Version: 0.1
Author: Maxwell
Date: 2024-05-07
"""

from math import sqrt


def is_prime(n):
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True


# 试一试有什么不一样
# with open('prime.txt', 'a') as f:
with open('prime.txt', 'w') as f:
    for num in range(2, 100):
        if is_prime(num):
            f.write(str(num) + '\n')
print('写入完成!')