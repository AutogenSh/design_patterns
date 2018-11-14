'''
装饰器模式
主要解决：一般的，我们为了扩展一个类经常使用继承方式实现，由于继承为类引入静态特征，并且随着扩展功能的增多，子类会很膨胀。

何时使用：在不想增加很多子类的情况下扩展类。
'''


class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print('Shape: Circle')


class Rectangle(Shape):
    def draw(self):
        print('Shape: Rectangle')


class ShapeDecorator(Shape):
    def __init__(self, shape: Shape):
        self._shape = shape

    def draw(self):
        self._shape.draw()


class RedShapeDecorator(ShapeDecorator):
    def draw(self):
        super().draw()
        self.__setredborder()

    def __setredborder(self):
        print('Border Color: Red')


if __name__ == '__main__':
    circle = Circle()
    redcircle = RedShapeDecorator(Circle())
    redrect = RedShapeDecorator(Rectangle())

    print('\nCircle with normal border')
    circle.draw()

    print('\nCircle of red border')
    redcircle.draw()

    print('\nRectangle of red border')
    redrect.draw()

