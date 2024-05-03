"""
另一种创建类的方式

Version: 0.1
Author: Maxwell
Date : 2024-05-01
"""

def bar(self, name):
    self._name = name


def foo(self, course_name):
    print('%s正在学习%s.' % (self._name, course_name))

def main():
    Student = type('Student', (object,), dict(__init__=bar, study =foo))
    stu1 = Student('Maxwell')
    stu1.study('Python program design')

if __name__ == '__main__':
    main()