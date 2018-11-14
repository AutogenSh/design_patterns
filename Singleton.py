'''
单例模式
保证一个类仅有一个实例，并提供一个访问它的全局访问点。

主要解决：一个全局使用的类频繁地创建与销毁。

何时使用：当您想控制实例数目，节省系统资源的时候。

'''


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MsgBox(metaclass=Singleton):

    def __init__(self) -> None:
        self.ref = 1

    def showMessage(self):
        print("Hello World[%d]" % self.ref)
        self.ref += 1


class MsgBox2():

    def __init__(self) -> None:
        self.ref = 1

    def showMessage(self):
        print("Hello World[%d]" % self.ref)
        self.ref += 1


MsgBox().showMessage()
MsgBox().showMessage()
MsgBox().showMessage()
MsgBox().showMessage()
MsgBox2().showMessage()
MsgBox2().showMessage()
MsgBox2().showMessage()
MsgBox2().showMessage()
