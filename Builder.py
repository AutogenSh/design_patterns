'''
建造者模式
使用多个简单的对象一步一步构建成一个复杂的对象。

主要解决：由于需求的变化，这个复杂对象的各个部分经常面临着剧烈的变化，但是将它们组合在一起的算法却相对稳定。

何时使用：一些基本部件不会变，而其组合经常变化的时候。

'''

class Packing:
    def pack(self) -> str:
        pass


class Item:
    def name(self) -> str:
        pass

    def packing(self) -> Packing:
        pass

    def price(self) -> float:
        pass


####################################
class Wrapper(Packing):
    def pack(self) -> str:
        return 'Wrapper'


class Bottle(Packing):
    def pack(self) -> str:
        return 'Bottle'


####################################
class Burger(Item):
    def packing(self) -> Packing:
        return Wrapper()


class ColdDrink(Item):
    def packing(self) -> Packing:
        return Bottle()


####################################
class VegBurger(Burger):
    def name(self) -> str:
        return 'Veg Burger'

    def price(self) -> float:
        return 25.0


class ChickenBurger(Burger):
    def name(self) -> str:
        return 'Chicken Burger'

    def price(self) -> float:
        return 50.5


class Coke(ColdDrink):
    def name(self) -> str:
        return 'Coke'

    def price(self) -> float:
        return 30.0


class Pepsi(ColdDrink):
    def name(self) -> str:
        return 'Pepsi'

    def price(self) -> float:
        return 35.0


class Order:
    def __init__(self):
        self.items = {}

    def addItem(self, item):
        # if item in self.items.keys():
        #     self.items.append(item)
        pass

    def getCost(self):
        cost = 0
        for item in self.items:
            cost += item.price()
        return cost

    def showItems(self):
        for item in self.items:
            print('Item[%s] Pack[%s] Price[%.2f]' % (item.name(), item.packing().pack(), item.price()))


class OrderBuilder:
    def preparePack1(self):
        order = Order()
        order.addItem(VegBurger())
        order.addItem(Coke())
        order.addItem(VegBurger())
        order.addItem(Coke())
        return order

    def preparePack2(self):
        order = Order()
        order.addItem(ChickenBurger())
        order.addItem(Pepsi())
        order.addItem(ChickenBurger())
        order.addItem(Pepsi())
        return order


if __name__ == '__main__':
    # builder = OrderBuilder()
    #
    # order1 = builder.preparePack1()
    # print('Order A')
    # order1.showItems()
    # print('total: %.2f' % order1.getCost())
    #
    # print('----------------------------------------------------')
    #
    # order2 = builder.preparePack2()
    # print('Order B')
    # order2.showItems()
    # print('total: %.2f' % order2.getCost())
    #
    def addItem(items, item):
        if item in items.keys():
            items[item] += 1
        else:
            items[item] = 1


    items = {}
    burger = VegBurger()
    coke = Coke()

    addItem(items, burger)
    addItem(items, burger)
    addItem(items, coke)
    addItem(items, coke)
    addItem(items, coke)
    for item in items.keys():
        print('Name[%s] Pack[%s] Price[%.2f] Num[%d] Total[%.2f]' % \
              (item.name(), item.packing().pack(), item.price(), items[item], item.price() * items[item]))
