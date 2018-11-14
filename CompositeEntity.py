from abc import ABCMeta, abstractmethod

"""
组合实体模式（Composite Entity Pattern）用在 EJB 持久化机制中。一个组合实体是一个 EJB 实体 bean，代表了对象的图解。当更新一个组合实体时，内部依赖对象 beans 会自动更新，因为它们是由 EJB 实体 bean 管理的。以下是组合实体 bean 的参与者。

组合实体（Composite Entity） - 它是主要的实体 bean。它可以是粗粒的，或者可以包含一个粗粒度对象，用于持续生命周期。
粗粒度对象（Coarse-Grained Object） - 该对象包含依赖对象。它有自己的生命周期，也能管理依赖对象的生命周期。
依赖对象（Dependent Object） - 依赖对象是一个持续生命周期依赖于粗粒度对象的对象。
策略（Strategies） - 策略表示如何实现组合实体。



"""

class DependentObject1:
    def __init__(self, data=None):
        self.data = data
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data

class DependentObject2:
    def __init__(self, data=None):
        self.data = data
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data

class CoarseGrainedObject:
    def __init__(self):
        self.do1 = DependentObject1()
        self.do2 = DependentObject2()

    def setData(self, data1, data2):
        self.do1.setData(data1)
        self.do2.setData(data2)

    def getData(self):
        return [self.do1.getData(), self.do2.getData()]


class CompositeEntity:
    def __init__(self):
        self.cgo = CoarseGrainedObject()

    def setData(self, data1, data2):
        self.cgo.setData(data1, data2)

    def getData(self):
        return self.cgo.getData()


class Client:
    def __init__(self):
        self.composite = CompositeEntity()

    def printData(self):
        for data in self.composite.getData():
            print('Data: ' + data)

    def setData(self, data1, data2):
        self.composite.setData(data1, data2)


if __name__ == '__main__':
    client = Client()
    client.setData('Test', 'Data')
    client.printData()
    client.setData('Second Test', 'Data1')
    client.printData()



