from abc import abstractmethod

'''
工厂模式
定义一个创建对象的接口，让其子类自己决定实例化哪一个工厂类，工厂模式使其创建过程延迟到子类进行。

主要解决：主要解决接口选择的问题。

何时使用：我们明确地计划不同条件下创建不同实例时。

'''


class Shape():
    @abstractmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Inside Rectangle::draw() method.")


class Square(Shape):
    def draw(self):
        print("Inside Square::draw() method.")


class Circle(Shape):
    def draw(self):
        print("Inside Circle::draw() method.")


class ShapeFactory:
    def getShape(shapeType):
        if shapeType == "circle":
            return Circle()
        elif shapeType == "rect":
            return Rectangle()
        elif shapeType == "square":
            return Square()
        else:
            return None


s1 = ShapeFactory.getShape('circle')
s1.draw()

s2 = ShapeFactory.getShape('rect')
s2.draw()

s3 = ShapeFactory.getShape('square')
s3.draw()
