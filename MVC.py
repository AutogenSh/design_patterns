"""
MVC 模式代表 Model-View-Controller（模型-视图-控制器） 模式。这种模式用于应用程序的分层开发。

Model（模型） - 模型代表一个存取数据的对象或 JAVA POJO。它也可以带有逻辑，在数据变化时更新控制器。
View（视图） - 视图代表模型包含的数据的可视化。
Controller（控制器） - 控制器作用于模型和视图上。它控制数据流向模型对象，并在数据变化时更新视图。它使视图与模型分离开。

"""


class Student:
    def __init__(self):
        self.rollno = None
        self.name = None

    def getRollNo(self):
        return self.rollno

    def setRollNo(self, rollno):
        self.rollno = rollno

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name


class StudentView:
    def printStudentDetails(self, name, rollno):
        print("Student: ")
        print("Name: " + name)
        print("Roll No: " + rollno)


class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def setStudentName(self, name):
        self.model.setName(name)

    def getStudentName(self):
        return self.model.getName()

    def setStudentRollNo(self, rollno):
        self.model.setRollNo(rollno)

    def getStudentRollNo(self):
        return self.model.getRollNo()

    def updateView(self):
        self.view.printStudentDetails(self.model.getName(), self.model.getRollNo())


if __name__ == '__main__':
    def retriveStudentFromDatabase():
        student = Student()
        student.setName('Robert')
        student.setRollNo('10')
        return student


    model = retriveStudentFromDatabase()
    view = StudentView()
    controller = StudentController(model, view)
    controller.updateView()
    print()
    controller.setStudentName('John')
    controller.updateView()
