from abc import ABCMeta, abstractmethod

"""

前端控制器模式（Front Controller Pattern）是用来提供一个集中的请求处理机制，所有的请求都将由一个单一的处理程序处理。
该处理程序可以做认证/授权/记录日志，或者跟踪请求，然后把请求传给相应的处理程序。以下是这种设计模式的实体。

前端控制器（Front Controller） - 处理应用程序所有类型请求的单个处理程序，应用程序可以是基于 web 的应用程序，也可以是基于桌面的应用程序。
调度器（Dispatcher） - 前端控制器可能使用一个调度器对象来调度请求到相应的具体处理程序。
视图（View） - 视图是为请求而创建的对象。

我们将创建 FrontController、Dispatcher 分别当作前端控制器和调度器。
HomeView 和 StudentView 表示各种为前端控制器接收到的请求而创建的视图。

FrontControllerPatternDemo，我们的演示类使用 FrontController 来演示前端控制器设计模式。

"""

class HomeView:
    def show(self):
        print('Displaying Home Page')

class StudentView:
    def show(self):
        print('Displaying Student Page')

class Dispatcher:
    def __init__(self):
        self.home = HomeView()
        self.stu = StudentView()

    def dispatche(self, req):
        if req == 'student':
            self.stu.show()
        else:
            self.home.show()


class FrontController:
    def __init__(self):
        self.dispatcher = Dispatcher()

    def isAuthenticUser(self) -> bool:
        print('User is authenticated successfully.')
        return True

    def trackRequest(self, request):
        print('Page requested: ' + request)

    def dispatchRequest(self, request):
        self.trackRequest(request)
        if (self.isAuthenticUser()):
            self.dispatcher.dispatche(request)

if __name__ == '__main__':
    controller = FrontController()
    controller.dispatchRequest('HOME')
    controller.dispatchRequest('STUDENT')




