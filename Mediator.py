import time

"""
中介者模式（Mediator Pattern）是用来降低多个对象和类之间的通信复杂性。
这种模式提供了一个中介类，该类通常处理不同类之间的通信，并支持松耦合，使代码易于维护。
中介者模式属于行为型模式。


主要解决：对象与对象之间存在大量的关联关系，这样势必会导致系统的结构变得很复杂，同时若一个对象发生改变，我们也需要跟踪与之相关联的对象，同时做出相应的处理。

何时使用：多个类相互耦合，形成了网状结构。

如何解决：将上述网状结构分离为星型结构。

关键代码：对象 Colleague 之间的通信封装到一个类中单独处理。

应用实例： 
1、中国加入 WTO 之前是各个国家相互贸易，结构复杂，现在是各个国家通过 WTO 来互相贸易。 
2、机场调度系统。 3、MVC 框架，其中C（控制器）就是 M（模型）和 V（视图）的中介者。

"""

class ChatRoom:
    @staticmethod
    def show(user, message):
        print('[%s] %s: %s' % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), user.getName(), message))


class User:
    def __init__(self, name=None):
        self.name = name

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def sendMessage(self, message):
        ChatRoom.show(self, message)


if __name__ == '__main__':
    robert = User('robert')
    john = User('John')

    robert.sendMessage('Hi! John!')
    john.sendMessage('Hello! Robert!')


