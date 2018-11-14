"""
外观模式

主要解决：降低访问复杂系统的内部子系统时的复杂度，简化客户端与之的接口。

何时使用：
1、客户端不需要知道系统内部的复杂联系，整个系统只需提供一个"接待员"即可。
2、定义系统的入口。
"""


class Shape:
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print('Rectangle::draw()')


class Square(Shape):
    def draw(self):
        print('Square::draw()')


class Circle(Shape):
    def draw(self):
        print('Circle::draw()')


class ShapeMaker:
    def __init__(self) -> None:
        self.circle = Circle()
        self.rect = Rectangle()
        self.square = Square()

    def drawcircle(self):
        self.circle.draw()

    def drawrect(self):
        self.rect.draw()

    def drawsquare(self):
        self.square.draw()


if __name__ == '__main__':
    maker = ShapeMaker()
    maker.drawcircle()
    maker.drawrect()
    maker.drawsquare()
