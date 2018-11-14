from abc import abstractmethod

'''
迭代器模式（Iterator Pattern）是 Java 和 .Net 编程环境中非常常用的设计模式。
这种模式用于顺序访问集合对象的元素，不需要知道集合对象的底层表示。

意图：提供一种方法顺序访问一个聚合对象中各个元素, 而又无须暴露该对象的内部表示。

主要解决：不同的方式来遍历整个整合对象。

何时使用：遍历一个聚合对象。

如何解决：把在元素之间游走的责任交给迭代器，而不是聚合对象。

关键代码：定义接口：hasNext, next。
'''


class Iterator:
    @abstractmethod
    def hasNext(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> object:
        pass


class Container:
    @abstractmethod
    def iter(self) -> Iterator:
        pass


class GeneralIterator(Iterator):

    def __init__(self, list) -> None:
        super().__init__()
        self.index = 0
        self.list = list

    def hasNext(self) -> bool:
        if self.index < len(self.list):
            return True
        return False

    def next(self) -> object:
        if self.hasNext():
            obj = self.list[self.index]
            self.index += 1
            return obj


class NameRepository(Container):
    def __init__(self) -> None:
        self.names = ['Robert', 'John', 'Julie', 'Lora']

    def iter(self) -> Iterator:
        return GeneralIterator(self.names)


if __name__ == '__main__':
    repository = NameRepository()
    it = repository.iter()
    while (it.hasNext()):
        print('%s' % it.next())

