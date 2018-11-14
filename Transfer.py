"""

传输对象模式（Transfer Object Pattern）用于从客户端向服务器一次性传递带有多个属性的数据。传输对象也被称为数值对象。传输对象是一个具有 getter/setter 方法的简单的 POJO 类，它是可序列化的，所以它可以通过网络传输。它没有任何的行为。服务器端的业务类通常从数据库读取数据，然后填充 POJO，并把它发送到客户端或按值传递它。对于客户端，传输对象是只读的。客户端可以创建自己的传输对象，并把它传递给服务器，以便一次性更新数据库中的数值。以下是这种设计模式的实体。

业务对象（Business Object） - 为传输对象填充数据的业务服务。
传输对象（Transfer Object） - 简单的 POJO，只有设置/获取属性的方法。
客户端（Client） - 客户端可以发送请求或者发送传输对象到业务对象。

"""


class StudentVO:
    def __init__(self, name=None, rollno=None):
        self.name = name
        self.rollno = rollno

    def getName(self):
        return self.name

    def getRollno(self):
        return self.rollno

    def setName(self, name):
        self.name = name

    def setRollno(self, rollno):
        self.rollno = rollno


class StudentBO:
    def __init__(self):
        self.students = []
        stu1 = StudentVO('Robert', 0)
        stu2 = StudentVO('John', 1)
        self.students.append(stu1)
        self.students.append(stu2)

    def deleteStudent(self, stu):
        self.students.pop(stu.getRollno())
        print('Student: Roll No[%d] Name[%s], deleted from database' % (stu.getRollno(), stu.getName()))

    def getAllStudents(self):
        return self.students

    def getStudent(self, rollno):
        return self.students[rollno]

    def updateStudent(self, stu):
        self.students[stu.getRollno()].setName(stu.getName())
        print('Student: Roll No[%d] Name[%s], updated in the database' % (stu.getRollno(), stu.getName()))


if __name__ == '__main__':
    stuBO = StudentBO()
    for vo in stuBO.getAllStudents():
        print('Student: Roll No[%d] Name[%s]' % (vo.getRollno(), vo.getName()))

    print('=======================================\n更新:')
    stuVO = stuBO.getAllStudents()[0]
    stuVO.setName('Micheal')
    stuBO.updateStudent(stuVO)

    stuVO = stuBO.getAllStudents()[0]
    print('Student: Roll No[%d] Name[%s]' % (stuVO.getRollno(), stuVO.getName()))
