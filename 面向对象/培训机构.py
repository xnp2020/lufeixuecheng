class School(object):
    def __init__(self,name,addr) -> None:
        self.name = name
        self.addr = addr

class Course(object):
    def __init__(self,name,school,teacher,fee) -> None:
        self.name = name
        self.school = school
        self.teacher = teacher
        self.fee = fee

class Teacher(object):
    def __init__(self,name,school,course,clazz) -> None:
        self.name = name
        self.school = school
        self.course = course
        self.clazz = clazz

c