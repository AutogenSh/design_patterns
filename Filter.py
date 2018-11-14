'''
过滤器模式

这种模式允许开发人员使用不同的标准来过滤一组对象，
通过逻辑运算以解耦的方式把它们连接起来。
这种类型的设计模式属于结构型模式，它结合多个标准来获得单一标准。
'''


class Person:
    def __init__(self, name, gender, maritalStatus):
        self.name = name
        self.gender = gender
        self.maritalStatus = maritalStatus

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

    def getMaritalStatus(self):
        return self.maritalStatus

    def __str__(self):
        return 'Person : [ Name : %s, Gender : %s, Marital Status : %s]' % (self.name, self.gender, self.maritalStatus)


class Criteria:
    def criteria(self, persons):
        pass


class Male(Criteria):
    def criteria(self, persons):
        _persons = []
        for person in persons:
            if person.getGender().lower() == 'male':
                _persons.append(person)
        return _persons


class Female(Criteria):
    def criteria(self, persons):
        _persons = []
        for person in persons:
            if person.getGender().lower() == 'female':
                _persons.append(person)
        return _persons


class Single(Criteria):
    def criteria(self, persons):
        _persons = []
        for person in persons:
            if person.getMaritalStatus().lower() == 'single':
                _persons.append(person)
        return _persons


class And(Criteria):
    def __init__(self, one: Criteria, other: Criteria):
        self.one = one
        self.other = other

    def criteria(self, persons):
        _persons = self.one.criteria(persons)
        return self.other.criteria(_persons)


class Or(Criteria):
    def __init__(self, one: Criteria, other: Criteria):
        self.one = one
        self.other = other

    def criteria(self, persons):
        _persons1 = self.one.criteria(persons)
        _persons2 = self.other.criteria(persons)
        return set(_persons1).union(_persons2)


def printPersons(list):
    for p in list:
        print(p)


if __name__ == '__main__':
    persons = [
        Person("Robert", "Male", "Single"),
        Person("John", "Male", "Married"),
        Person("Laura", "Female", "Married"),
        Person("Diana", "Female", "Single"),
        Person("Mike", "Male", "Single"),
        Person("Bobby", "Male", "Single")
    ]
    male = Male()
    female = Female()
    single = Single()
    singleMale = And(single, male)
    singleOrFemale = Or(single, female)

    print('Males: ')
    printPersons(male.criteria(persons))

    print('\nFemales: ')
    printPersons(female.criteria(persons))

    print('\nSingle Males: ')
    printPersons(singleMale.criteria(persons))

    print('\nSingle or Females: ')
    printPersons(singleOrFemale.criteria(persons))
