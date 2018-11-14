"""
在空对象模式（Null Object Pattern）中，一个空对象取代 NULL 对象实例的检查。Null 对象不是检查空值，而是反应一个不做任何动作的关系。这样的 Null 对象也可以在数据不可用的时候提供默认的行为。

在空对象模式中，我们创建一个指定各种要执行的操作的抽象类和扩展该类的实体类，还创建一个未对该类做任何实现的空对象类，该空对象类将无缝地使用在需要检查空值的地方。


我们将创建一个定义操作（在这里，是客户的名称）的 AbstractCustomer 抽象类，和扩展了 AbstractCustomer 类的实体类。工厂类 CustomerFactory 基于客户传递的名字来返回 RealCustomer 或 NullCustomer 对象。

NullPatternDemo，我们的演示类使用 CustomerFactory 来演示空对象模式的用法。

"""
from abc import ABCMeta, abstractmethod


class AbstractCustomer(metaclass=ABCMeta):
    def __init__(self, name=None):
        self.name = name

    @abstractmethod
    def isNil(self):
        pass

    @abstractmethod
    def getName(self):
        pass


class RealCustomer(AbstractCustomer):
    def __init__(self, name=None):
        super().__init__(name)

    def isNil(self):
        return False

    def getName(self):
        return self.name


class NullCustomer(AbstractCustomer):
    def __init__(self):
        super().__init__()

    def isNil(self):
        return True

    def getName(self):
        return 'Not Available in Customer Database'


class CustomFactory:
    names = [name.lower() for name in ['Rob', 'Joe', 'Julie']]

    @classmethod
    def getCustomer(cls, name):
        if name.lower() in cls.names:
            return RealCustomer(name)
        else:
            return NullCustomer()


if __name__ == '__main__':
    customer1 = CustomFactory.getCustomer('Rob')
    customer2 = CustomFactory.getCustomer('Bob')
    customer3 = CustomFactory.getCustomer('Julie')
    customer4 = CustomFactory.getCustomer('Laura')

    print('Customers:\n===================')
    print(customer1.getName())
    print(customer2.getName())
    print(customer3.getName())
    print(customer4.getName())



