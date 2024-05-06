"""
definition and use student class

Version: 0.1
Author: Maxwell
Date: 2024-05-03
"""

def _foo():
    print('test')

class Student(object):

    # __init__ is a special method to initialize when once create object.
    # according to initial method to binding two attributes(name & age) for student object

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8 requires identifiers to be named in all lowercase with multiple words connected by underscores.
    # Many programmers and companies prefer to use camel case naming convention(camelCase identifiers)

    def watch_av(self):
        if self.age < 18:
            print('%s I can only watch 《Paw Patrol》' % self.name)
        else:
            print('%s watching Japan action movies.' % self.name)
        
def main():
    # create student object,then give it name and age.
    stu1 = Student('Maxwell', 26)
    # send study message to object
    stu1.study('Python program design')
    # send watch_av message to object
    stu1.watch_av()
    stu2 = Student('christine', 31)
    stu2.study('think is good')
    stu2.watch_av()

if __name__ == '__main__':
    main()
