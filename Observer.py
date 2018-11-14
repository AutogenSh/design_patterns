"""
观察者模式

当对象间存在一对多关系时，则使用观察者模式（Observer Pattern）。
比如，当一个对象被修改时，则会自动通知它的依赖对象。
观察者模式属于行为型模式。


意图：定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新。

主要解决：一个对象状态改变给其他对象通知的问题，而且要考虑到易用和低耦合，保证高度的协作。

何时使用：一个对象（目标对象）的状态发生改变，所有的依赖对象（观察者对象）都将得到通知，进行广播通知。

如何解决：使用面向对象技术，可以将这种依赖关系弱化。

"""


class Subject:
    def __init__(self):
        self.state = None
        self.observers = []

    def getstate(self):
        return self.state

    def setstate(self, state):
        self.state = state
        self.notify()

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self):
        for ob in self.observers:
            ob.update()


class Observer:
    def __init__(self, subject=None):
        self.subject: Subject = subject

    def update(self):
        pass


class BinaryObserver(Observer):
    def __init__(self, subject):
        super().__init__(subject)
        self.subject.attach(self)

    def update(self):
        print('Binary String: ', bin(self.subject.getstate()))


class OctalObserver(Observer):
    def __init__(self, subject):
        super().__init__(subject)
        self.subject.attach(self)

    def update(self):
        print('Octal String: ', oct(self.subject.getstate()))


class HexaObserver(Observer):
    def __init__(self, subject):
        super().__init__(subject)
        self.subject.attach(self)

    def update(self):
        print('Binary String: ', hex(self.subject.getstate()))


if __name__ == '__main__':
    subject = Subject()

    b = BinaryObserver(subject)
    o = OctalObserver(subject)
    h = HexaObserver(subject)

    print('First state change: 15')
    subject.setstate(15)
    print()
    print('Second state change: 10')
    subject.setstate(10)
