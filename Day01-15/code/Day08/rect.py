"""
definition and use the traingle class

Version: 0.1
Author: Maxwell
Date: 2024-05-03
"""

class Rect(object):
    """traingle class"""

    def __init__(self, width=0, height=0):
        """initial method"""
        self.__width = width
        self.__height = height

    def perimeter(self):
        """calculate perimeter"""
        return (self.__width + self.__height) * 2
    
    def area(self):
        """Calculate area"""
        return self.__width * self.__height
    

    def __str__(self):
        """ the string express of rectangle object """
        return 'rectangle[%f,%f]' % (self.__width, self.__height)
    
    def __del__(self):
        """constructor"""
        print('destroy rectangle object')

    
if __name__ == '__main__':
    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(3.5, 4.5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())