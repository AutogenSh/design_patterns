from abc import ABCMeta, abstractmethod

"""
业务代表模式（Business Delegate Pattern）用于对表示层和业务层解耦。它基本上是用来减少通信或对表示层代码中的业务层代码的远程查询功能。在业务层中我们有以下实体。

客户端（Client） - 表示层代码可以是 JSP、servlet 或 UI java 代码。
业务代表（Business Delegate） - 一个为客户端实体提供的入口类，它提供了对业务服务方法的访问。
查询服务（LookUp Service） - 查找服务对象负责获取相关的业务实现，并提供业务对象对业务代表对象的访问。
业务服务（Business Service） - 业务服务接口。实现了该业务服务的实体类，提供了实际的业务实现逻辑。


"""


class BusinessService(metaclass=ABCMeta):
    @abstractmethod
    def doProcessing(self):
        pass


class EJBService(BusinessService):
    def doProcessing(self):
        print('Processing task by invoking EJB Service')


class JMSService(BusinessService):
    def doProcessing(self):
        print('Processing task by invoking JMS Service')


class BusinessLookUp:
    def getBusinessService(self, type):
        if type == 'EJB':
            return EJBService()
        elif type == 'JMS':
            return JMSService()
        return None


class BusinessDelegate:
    def __init__(self):
        self.lookup = BusinessLookUp()
        self.type = None

    def setType(self, type):
        self.type = type

    def doTask(self):
        service = self.lookup.getBusinessService(self.type)
        service.doProcessing()


class Client:
    def __init__(self, service):
        self.service = service

    def doTask(self):
        self.service.doTask()


if __name__ == '__main__':
    delegate = BusinessDelegate()
    delegate.setType('EJB')

    client = Client(delegate)
    client.doTask()

    delegate.setType('JMS')
    client.doTask()










