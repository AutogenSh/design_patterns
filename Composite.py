'''
组合模式
又叫部分整体模式，是用于把一组相似的对象当作一个单一的对象

主要解决：它在我们树型结构的问题中，模糊了简单元素和复杂元素的概念，客户程序可以向处理简单元素一样来处理复杂元素，从而使得客户程序与复杂元素的内部结构解耦。

何时使用： 1、您想表示对象的部分-整体层次结构（树形结构）。 2、您希望用户忽略组合对象与单个对象的不同，用户将统一地使用组合结构中的所有对象。

'''


class employee:
    def __init__(self, name, department, salary):
        self.__name = name
        self.__department = department
        self.__salary = salary
        self.__subordinates = []

    def add(self, e):
        self.__subordinates.append(e)

    def remove(self, e):
        self.__subordinates.remove(e)

    def subordinates(self):
        return self.__subordinates

    def __str__(self):
        return 'Employee :[ Name : %s, dept : %s, salary :%d]' % (self.__name, self.__department, self.__salary)


if __name__ == '__main__':
    CEO = employee("John", "CEO", 30000)
    headSales = employee("Robert", "Head Sales", 20000)

    headMarketing = employee("Michel", "Head Marketing", 20000)

    clerk1 = employee("Laura", "Marketing", 10000)
    clerk2 = employee("Bob", "Marketing", 10000)

    salesExecutive1 = employee("Richard", "Sales", 10000)
    salesExecutive2 = employee("Rob", "Sales", 10000)

    CEO.add(headSales)
    CEO.add(headMarketing)

    headSales.add(salesExecutive1)
    headSales.add(salesExecutive2)

    headMarketing.add(clerk1)
    headMarketing.add(clerk2)

    print(CEO)
    for e1 in CEO.subordinates():
        print(e1)
        for e2 in e1.subordinates():
            print(e2)

