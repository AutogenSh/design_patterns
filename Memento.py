"""
备忘录模式（Memento Pattern）保存一个对象的某个状态，以便在适当的时候恢复对象。
备忘录模式属于行为型模式。

意图：在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。

主要解决：所谓备忘录模式就是在不破坏封装的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态，这样可以在以后将对象恢复到原先保存的状态。

何时使用：很多时候我们总是需要记录一个对象的内部状态，这样做的目的就是为了允许用户取消不确定或者错误的操作，能够恢复到他原先的状态，使得他有"后悔药"可吃。

如何解决：通过一个备忘录类专门存储对象状态。

"""


class Originator:
    def __init__(self):
        self.state = None

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state

    def save(self):
        return Memento(self.state)

    def restore(self, memento):
        self.state = memento.getState()


class Memento:
    def __init__(self, state=None):
        self.state = state

    def getState(self):
        return self.state


class CareTaker:
    def __init__(self):
        self.mementos = []

    def add(self, memento):
        self.mementos.append(memento)

    def get(self, index):
        return self.mementos[index]


if __name__ == '__main__':
    caretake = CareTaker()
    originator = Originator()

    originator.setState(1)
    originator.setState(2)
    caretake.add(originator.save())
    originator.setState(3)
    caretake.add(originator.save())
    originator.setState(4)

    print('current state: %d' % originator.getState())
    print('#0 state: %d' % caretake.get(0).getState())
    print('#1 state: %d' % caretake.get(1).getState())


