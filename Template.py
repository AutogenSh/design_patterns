from abc import ABCMeta, abstractmethod

"""

在模板模式（Template Pattern）中，一个抽象类公开定义了执行它的方法的方式/模板。
它的子类可以按需要重写方法实现，但调用将以抽象类中定义的方式进行。
这种类型的设计模式属于行为型模式。

意图：定义一个操作中的算法的骨架，而将一些步骤延迟到子类中。
w模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤。
主要解决：一些方法通用，却在每一个子类都重新写了这一方法。
何时使用：有一些通用的方法。
如何解决：将这些通用算法抽象出来。

"""


class Game(metaclass=ABCMeta):
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def end(self):
        pass

    def play(self):
        self.initialize()
        self.start()
        self.end()


class Cricket(Game):

    def initialize(self):
        print('Cricket Game Initialized! Start playing.')

    def start(self):
        print('Cricket Game Started. Enjoy the game!')

    def end(self):
        print('Cricket Game Finished!')


class Footbal(Game):

    def initialize(self):
        print('Football Game Initialized! Start playing.')

    def start(self):
        print('Football Game Started. Enjoy the game!')

    def end(self):
        print('Football Game Finished!')


if __name__ == '__main__':
    game = Cricket()
    game.play()
    print()
    game = Footbal()
    game.play()
