from abc import ABC, abstractmethod


class GeometricShape(ABC):
    PI = 3.14

    @abstractmethod
    def area(self):
        raise NotImplementedError

    def describe(self):
        print('Probably has corners')


class Square(GeometricShape, ABC):

    def __init__(self, side):
        self.__side = side

    @property
    def side(self):
        return self.__side

    @side.getter
    def side(self):
        print(f'Getter: The side is: {self.__side}')
        return self.__side

    @side.setter
    def side(self, side):
        print(f'Setter: The new side is: {side}')
        self.__side = side

    @side.deleter
    def side(self):
        print('Side deleted')
        self.__side = None

    def area(self):
        print(f'The square area is: {self.__side ** 2}')


class Circle(GeometricShape, ABC):

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.getter
    def radius(self):
        print(f'Getter: The radius is: {self.__radius}')
        return self.__radius

    @radius.setter
    def radius(self, radius):
        print(f'Setter: The new radius is: {radius}')
        self.__radius = radius


    @radius.deleter
    def radius(self):
        print('Deleter: Radius deleted')
        self.__radius = None

    def area(self):
        print(f'The circle area is: {GeometricShape.PI * (self.__radius ** 2)}')

    def describe(self):
        print('Without corners')


circle1 = Circle(100)
circle1.radius
circle1.radius = 50
circle1.area()
del circle1.radius
circle1.radius


square1 = Square(50)
square1.side
square1.side = 10
square1.area()
del square1.side
square1.side




