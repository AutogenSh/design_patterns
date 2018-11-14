"""
在状态模式（State Pattern）中，类的行为是基于它的状态改变的。这种类型的设计模式属于行为型模式。

在状态模式中，我们创建表示各种状态的对象和一个行为随着状态对象改变而改变的 context 对象。

意图：允许对象在内部状态发生改变时改变它的行为，对象看起来好像修改了它的类。

主要解决：对象的行为依赖于它的状态（属性），并且可以根据它的状态改变而改变它的相关行为。

何时使用：代码中包含大量与对象状态有关的条件语句。

如何解决：将各种具体的状态类抽象出来。
"""
from abc import abstractmethod, ABCMeta


class State(metaclass=ABCMeta):
    @abstractmethod
    def doAction(self, context):
        pass


class StartState(State):
    def doAction(self, context):
        print('Player is in start state')
        context.setState(self)

    def __str__(self):
        return 'Start State'


class StopState(State):
    def doAction(self, context):
        print('Player is in stop state')
        context.setState(self)

    def __str__(self):
        return 'Stop State'


class Context:
    def __init__(self, state=None):
        self.state = state

    def setState(self, state=None):
        self.state = state

    def getState(self):
        return self.state


if __name__ == '__main__':
    context = Context()

    start = StartState()
    start.doAction(context)
    print(context.getState())

    stop = StopState()
    stop.doAction(context)
    print(context.getState())


