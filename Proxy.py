"""
代理模式
在代理模式中，我们创建具有现有对象的对象，以便向外界提供功能接口。
一个类代表另一个类的功能。

主要解决：
在直接访问对象时带来的问题，
比如说：要访问的对象在远程的机器上。
在面向对象系统中，有些对象由于某些原因（比如对象创建开销很大，或者某些操作需要安全控制，或者需要进程外的访问），
直接访问会给使用者或者系统结构带来很多麻烦，我们可以在访问此对象时加上一个对此对象的访问层。

何时使用：想在访问一个类时做一些控制。

"""


class Image:
    def display(self):
        pass


class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.loadfromdisk()

    def display(self):
        print('Displaying', self.filename)

    def loadfromdisk(self):
        print('Loading', self.filename)


class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.realimg = None

    def display(self):
        if self.realimg is None:
            self.realimg = RealImage(self.filename)
        self.realimg.display()


if __name__ == '__main__':
    image = ProxyImage('/tmp/test_10mb.jpg')

    # 读磁盘
    image.display()

    # 不需要读磁盘
    print()
    image.display()

