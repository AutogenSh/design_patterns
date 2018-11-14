from abc import ABCMeta, abstractmethod

"""
在访问者模式（Visitor Pattern）中，我们使用了一个访问者类，它改变了元素类的执行算法。
通过这种方式，元素的执行算法可以随着访问者改变而改变。这种类型的设计模式属于行为型模式。
根据模式，元素对象已接受访问者对象，这样访问者对象就可以处理元素对象上的操作。

意图：主要将数据结构与数据操作分离。

主要解决：稳定的数据结构和易变的操作耦合问题。

何时使用：需要对一个对象结构中的对象进行很多不同的并且不相关的操作，而需要避免让这些操作"污染"这些对象的类，使用访问者模式将这些封装到类中。

如何解决：在被访问的类里面加一个对外提供接待访问者的接口。

"""


class ComputerPart(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class Computer(ComputerPart):

    def accept(self, visitor):
        visitor.visit(self)


class Keyboard(ComputerPart):

    def accept(self, visitor):
        visitor.visit(self)


class Mouse(ComputerPart):

    def accept(self, visitor):
        visitor.visit(self)


class Monitor(ComputerPart):

    def accept(self, visitor):
        visitor.visit(self)


class ComputerPartVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, computerpart):
        pass


class ComputerPartDisplayVisitor(ComputerPartVisitor):
    def visit(self, computerpart):
        if isinstance(computerpart, Computer):
            print('Displaying Computer.')
        elif isinstance(computerpart, Keyboard):
            print('Displaying Keyboard.')
        elif isinstance(computerpart, Mouse):
            print('Displaying Mouse.')
        elif isinstance(computerpart, Monitor):
            print('Displaying Monitor.')


if __name__ == '__main__':
    computer = Computer()
    computer.accept(ComputerPartDisplayVisitor())
