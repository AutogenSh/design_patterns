'''
桥接模式
用于把抽象化与实现化解耦，使得二者可以独立变化。

主要解决：在有多种可能会变化的情况下，用继承会造成类爆炸问题，扩展起来不灵活。

何时使用：实现系统可能有多个角度分类，每一种角度都可能变化。

'''


class DrawAPI:
    def draw_circle(self, radius, x, y):
        pass


class Red(DrawAPI):
    def draw_circle(self, radius, x, y):
        print('Drawing Circle[ color: red, radius: %d, x: %d, y: %d]' % (radius, x, y))


class Green(DrawAPI):
    def draw_circle(self, radius, x, y):
        print('Drawing Circle[ color: green, radius: %d, x: %d, y: %d]' % (radius, x, y))


class Shape:
    def __init__(self, drawapi) -> None:
        self.drawapi = drawapi

    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, radius, drawapi) -> None:
        super().__init__(drawapi)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        self.drawapi.draw_circle(self.radius, self.x, self.y)


if __name__ == '__main__':
    redcircle = Circle(100, 100, 10, Red())
    greencircle = Circle(100, 100, 10, Green())

    redcircle.draw()
    greencircle.draw()
