"""
从文本文件中读取数据

Version: 0.1
Author: Maxwell
Date: 2024-05-07
"""

import time

def main():
    # 一次性读取整个文件内容
    with open('tree.txt','r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in 循环逐行读取
    with open('tree.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('tree.txt') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main()