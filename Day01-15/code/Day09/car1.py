"""
the use of attributions
-- acessor/modifier/deleter
-- use __slots__ to limit for attributions.

Version: 0.1
Author: Maxwell
Date: 2024-05-06

"""
class Car(object):

    __slots__ = ('_brand', '_max_speed')

    def __init__(self, brand, max_speed):
        self.brand = brand
        self._max_speed = max_speed

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @brand.deleter
    def brand(self):
        del self._brand
    
    @property
    def max_speed(self):
        return self._max_speed
    
    @max_speed.setter
    def max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car: [品牌=%s, 最高时速=%d]' % (self._brand, self._max_speed)
    
car = Car('QQ', 120)
print(car)
#ValueError
# car.max_speed = -100
car.max_speed = 320
car.brand = 'Benz'
# use __slots__ attribute to limit the following code will be generated exception.
# car.current_speed = 80
print(car)
# if deletor be provided, we can execute the following code.
# del car.brand
# the dream of the attribution.
print(Car.brand)
print(Car.brand.fget)
print(Car.brand.fset)
print(Car.brand.fdel)