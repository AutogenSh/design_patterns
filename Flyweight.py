"""
享元模式（Flyweight Pattern）主要用于减少创建对象的数量，以减少内存占用和提高性能。
这种类型的设计模式属于结构型模式，它提供了减少对象数量从而改善应用所需的对象结构的方式。

意图：运用共享技术有效地支持大量细粒度的对象。

主要解决：在有大量对象时，有可能会造成内存溢出，我们把其中共同的部分抽象出来，如果有相同的业务请求，直接返回在内存中已有的对象，避免重新创建。

何时使用：
1、系统中有大量对象。
2、这些对象消耗大量内存。
3、这些对象的状态大部分可以外部化。
4、这些对象可以按照内蕴状态分为很多组，当把外蕴对象从对象中剔除出来时，每一组对象都可以用一个对象来代替。
5、系统不依赖于这些对象身份，这些对象是不可分辨的。

如何解决：用唯一标识码判断，如果在内存中有，则返回这个唯一标识码所标识的对象。

"""
import random


class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, color):
        self.color = color
        self.x = 0
        self.y = 0
        self.radius = 0

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def setradius(self, radius):
        self.radius = radius

    def draw(self):
        print('Circle: Draw() [Color:%s, x:%d, y:%d, radius:%d' % (self.color, self.x, self.y, self.radius))


class ShapeFactory:
    map = {}

    @staticmethod
    def circle(color):
        if color in ShapeFactory.map.keys():
            return ShapeFactory.map[color]
        else:
            c = Circle(color)
            ShapeFactory.map[color] = c
            print('Creating circle of color : %s' % color)
            return c


if __name__ == '__main__':
    colors = ["Red", "Green", "Blue", "White", "Black"]
    for i in range(20):
        circle = ShapeFactory.circle(random.choice(colors))
        circle.setx(random.randrange(0, 100, step=1))
        circle.sety(random.randrange(0, 100, step=1))
        circle.setradius(100)
        circle.draw()
        print()

