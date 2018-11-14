from abc import ABCMeta, abstractmethod

"""
数据访问对象模式（Data Access Object Pattern）或 DAO 模式用于把低级的数据访问 API 或操作从高级的业务服务中分离出来。以下是数据访问对象模式的参与者。

数据访问对象接口（Data Access Object Interface） - 该接口定义了在一个模型对象上要执行的标准操作。
数据访问对象实体类（Data Access Object concrete class） - 该类实现了上述的接口。该类负责从数据源获取数据，数据源可以是数据库，也可以是 xml，或者是其他的存储机制。
模型对象/数值对象（Model Object/Value Object） - 该对象是简单的 POJO，包含了 get/set 方法来存储通过使用 DAO 类检索到的数据。


我们将创建一个作为模型对象或数值对象的 Student 对象。StudentDao 是数据访问对象接口。
StudentDaoImpl 是实现了数据访问对象接口的实体类。
DaoPatternDemo，我们的演示类使用 StudentDao 来演示数据访问对象模式的用法。

"""


class Student:
    def __init__(self, name=None, rollno=None):
        self.name = name
        self.rollno = rollno

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getRollno(self):
        return self.rollno

    def setRollno(self, rollno):
        self.rollno = rollno

    def __str__(self):
        return 'Student: No[%d], Name[%s]' % (self.rollno, self.name)


class StudentDao(metaclass=ABCMeta):
    @abstractmethod
    def getAllStudents(self):
        pass

    @abstractmethod
    def getStudent(self, rollno):
        pass

    @abstractmethod
    def updateStudent(self, student):
        pass

    @abstractmethod
    def deleteStudent(self, student):
        pass


class StudentDaoImpl(StudentDao):
    def __init__(self):
        self.students = []
        self.students.append(Student('Robert', 0))
        self.students.append(Student('John', 0))

    def getAllStudents(self):
        return self.students

    def getStudent(self, rollno):
        return self.students[rollno]

    def updateStudent(self, student):
        self.students[student.getRollno()].setName(student.getName())
        print('Student: No[%d], updated' % student.getRollno())

    def deleteStudent(self, student):
        self.students.pop(student.getRollno())


if __name__ == '__main__':
    dao = StudentDaoImpl()

    for stu in dao.getAllStudents():
        print(stu)

    print('==============')
    stu = dao.getAllStudents()[0]
    stu.setName('Michael')
    dao.updateStudent(stu)

    for stu in dao.getAllStudents():
        print(stu)





