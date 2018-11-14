from abc import abstractmethod

"""
命令模式
命令模式（Command Pattern）是一种数据驱动的设计模式，它属于行为型模式。
请求以命令的形式包裹在对象中，并传给调用对象。
调用对象寻找可以处理该命令的合适的对象，并把该命令传给相应的对象，该对象执行命令。


意图：
将一个请求封装成一个对象，从而使您可以用不同的请求对客户进行参数化。

主要解决：
在软件系统中，行为请求者与行为实现者通常是一种紧耦合的关系，
但某些场合，比如需要对行为进行记录、撤销或重做、事务等处理时，
这种无法抵御变化的紧耦合的设计就不太合适。

何时使用：
在某些场合，比如要对行为进行"记录、撤销/重做、事务"等处理，这种无法抵御变化的紧耦合是不合适的。
在这种情况下，如何将"行为请求者"与"行为实现者"解耦？
将一组行为抽象为对象，可以实现二者之间的松耦合。

"""


class Order:
    @abstractmethod
    def execute(self):
        pass


class Stock:
    def __init__(self):
        self.name = 'ABC'
        self.quantity = 10

    def buy(self):
        print('Stock [ Name: %s, Quantity: %d ] bought' % (self.name, self.quantity))

    def sell(self):
        print('Stock [ Name: %s, Quantity: %d ] sold' % (self.name, self.quantity))


class BuyStock(Order):
    def __init__(self, stock) -> None:
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStock(Order):
    def __init__(self, stock) -> None:
        self.stock = stock

    def execute(self):
        self.stock.sell()


class Broker:
    def __init__(self) -> None:
        self.orders = []

    def takeOrder(self, order):
        self.orders.append(order)

    def placeOrders(self):
        for order in self.orders:
            order.execute()
        self.orders.clear()


if __name__ == '__main__':
    s = Stock()

    buy = BuyStock(s)
    sell = SellStock(s)

    broker = Broker()
    broker.takeOrder(buy)
    broker.takeOrder(sell)

    broker.placeOrders()
