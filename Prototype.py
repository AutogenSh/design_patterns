'''
原型模式
是用于创建重复的对象，同时又能保证性能。

主要解决：在运行期建立和删除原型。

何时使用：
1、当一个系统应该独立于它的产品创建，构成和表示时。
2、当要实例化的类是在运行时刻指定时，例如，通过动态装载。
3、为了避免创建一个与产品类层次平行的工厂类层次时。
4、当一个类的实例只能有几个不同状态组合中的一种时。
建立相应数目的原型并克隆它们可能比每次用合适的状态手工实例化该类更方便一些。

'''
import copy


class Shape:
    def __init__(self):
        self.__id = ''
        self._type = ''

    def draw(self):
        pass

    def getType(self):
        return self._type

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def clone(self):
        return copy.deepcopy(self)


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self._type = 'Rectangle'

    def draw(self):
        print('Inside Rectangle::draw() method.')

class Square(Shape):
    def __init__(self):
        super().__init__()
        self._type = 'Square'

    def draw(self):
        print('Inside Square::draw() method.')

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self._type = 'Circle'

    def draw(self):
        print('Inside Circle::draw() method.')


class ShapeCache:
    shapeMap = {}

    @classmethod
    def getShape(cls, id):
        shape = cls.shapeMap[id]
        return shape.clone()

    @classmethod
    def loadCache(cls):
        circle = Circle()
        circle.setId('1')
        cls.shapeMap[circle.getId()] = circle

        square = Square()
        square.setId('2')
        cls.shapeMap[square.getId()] = square

        rect = Rectangle()
        rect.setId('3')
        cls.shapeMap[rect.getId()] = rect

if __name__ == '__main__':
    ShapeCache.loadCache()

    shape1 = ShapeCache.getShape('1')
    shape2 = ShapeCache.getShape('2')
    shape3 = ShapeCache.getShape('3')
    shape11 = ShapeCache.getShape('1')
    shape21 = ShapeCache.getShape('2')
    shape31 = ShapeCache.getShape('3')

