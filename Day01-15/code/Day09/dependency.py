"""
对象之间的依赖关系和运算符重载

Version: 0.1
Author: Maxwell
Date: 2024-05-06
"""

class Car(object):

    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed
        self._current_speed = 0

    @property
    def brand(self):
        return self._brand
    
    def accelerate(self, delta):
        self._current_speed += delta
        if self._current_speed > self._max_speed:
            self._current_speed = self._max_speed

    def brake(self):
        self._current_speed = 0

    def __str__(self):
        return '%s当前的时速%d' % (self._brand, self._current_speed)
    
class Student(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    # there is existing dependent relationship between student and car --student use the car
    def drive(self, car):
        print('%s驾驶着%s欢快的行驶在去西天的路上' % (self._name, car._brand))
        car.accelerate(30)
        print(car)
        car.accelerate(50)
        print(car)
        car.accelerate(50)
        print(car)

    def study(self, course_name):
        print('%s正在学习%s.' % (self._name, course_name))
    
    def watch_av(self):
        if self._age < 18:
            print('%s只能观看《熊出没》.' % self._name)
        else:
            print('%s正在观看岛国爱情片' % self._name)
        
    # 重载大于（>）运算符
    def __gt__(self, other):
        return self._age > other._age
    
    # 重载大于（<）运算符
    def __lt__(self, other):
        return self._age < other._age
    
if __name__ == '__main__':
    stu1 = Student('Maxwell', 26)
    stu1.study('Python program design')
    stu1.watch_av()
    stu2 = Student('Python', 27)
    stu2.study('Think is good')
    stu2.watch_av()
    car = Car('QQ', 120)
    stu2.drive(car)
    print(stu1 > stu2)
    print(stu1 < stu2)
