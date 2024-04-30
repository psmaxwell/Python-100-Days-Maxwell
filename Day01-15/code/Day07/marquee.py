"""
输入学生考试成绩计算平均分

Version: 0.1
Author: Maxwell
Date: 2024-04-30
"""

import os
import time

def main():
    str = 'Welcome to Shanghai University Campus    '
    while True:
        print(str)
        time.sleep(0.2)
        str = str[1:] + str[0:1]
        # for windows use os.system('cls') instead
        os.system('clear')

if __name__ == '__main__':
    main()