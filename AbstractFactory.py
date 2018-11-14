'''
抽象工厂模式
抽象工厂模式（Abstract Factory Pattern）是围绕一个超级工厂创建其他工厂。该超级工厂又称为其他工厂的工厂。

主要解决：主要解决接口选择的问题。

何时使用：系统的产品有多于一个的产品族，而系统只消费其中某一族的产品。

'''


class Shape:
    def draw(self):
        pass


class Color:
    def fill(self):
        pass


class AbstractFactory:
    def getColor(self, shape):
        pass

    def getShape(self, color):
        pass


class Rectangle(Shape):
    def draw(self):
        print('Inside Rectangle::draw() method.')


class Square(Shape):
    def draw(self):
        print('Inside Square::draw() method.')


class Circle(Shape):
    def draw(self):
        print('Inside Circle::draw() method.')


class Red(Color):
    def fill(self):
        print('Inside Red::fill() method.')


class Green(Color):
    def fill(self):
        print('Inside Green::fill() method.')


class Blue(Color):
    def fill(self):
        print('Inside Blue::fill() method.')


class ShapeFactory(AbstractFactory):
    def getShape(self, shape):
        if shape == 'circle':
            return Circle()
        elif shape == 'rect':
            return Rectangle()
        elif shape == 'square':
            return Square()
        else:
            return None


class ColorFactory(AbstractFactory):
    def getColor(self, color):
        if color == 'red':
            return Red()
        elif color == 'green':
            return Green()
        elif color == 'blue':
            return Blue()
        else:
            return None


class FactoryProducer:
    def getFactory(self, factory):
        if factory == 'color':
            return ColorFactory()
        elif factory == 'shape':
            return ShapeFactory()
        else:
            return None


shapeFactory = FactoryProducer().getFactory('shape')
colorFactory = FactoryProducer().getFactory('color')

s1 = shapeFactory.getShape('circle')
s2 = shapeFactory.getShape('rect')
s3 = shapeFactory.getShape('square')
s1.draw()
s2.draw()
s3.draw()

c1 = colorFactory.getColor('red')
c2 = colorFactory.getColor('green')
c3 = colorFactory.getColor('blue')

c1.fill()
c2.fill()
c3.fill()
