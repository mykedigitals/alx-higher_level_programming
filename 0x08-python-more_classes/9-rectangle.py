#!/usr/bin/python3

"""Module that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the data for the rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """Prints a string representation of a rectangle with #"""

        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ''
        for row in range(self.__height):
            for col in range(self.__width):
                rect += str(self.print_symbol)
            rect += "\n"
        return rect[:-1]

    def __repr__(self):
        """Returns the name of the class with attributes"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Retrieves the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Defines the width of the rectangle
        Args:
            value: the integer that represents the width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Defines the height of the rectangle
        Args:
            value: the integer that represents the height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""

        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the perimiter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area"""

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""

        return Rectangle(size, size)
