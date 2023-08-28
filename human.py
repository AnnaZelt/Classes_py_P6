class Human:
    def __init__(self,age,name,sex) -> None:
        self.age = age
        self.name = name
        self.sex = sex

    def eat():
        print("eat")

    def sleep():
        print("sleep")

class Worker(Human):
    hours = 0
    efficiency = 0
    tasks = 0
    salary = 0
    
    def work(self):
        print("work")
    
    def __str__(self) -> str:
        return f"Sex: {self.sex}, Age: {self.age}"

class Student(Human):
    avgGrade = 0
    semester = ""

    def study(self):
        print("will this be on the test?")

    def __init__(self,age,name,sex,avg,semester) -> None:
        super().__init__(age,name,sex)
        self.avgGrade = avg
        self.semester = semester

    def __str__(self) -> str:
        return f"Sex: {self.sex}, Age: {self.age}"

class Manager(Worker):

    def __init__(self,age,name,sex) -> None:
        super().__init__(age,name,sex)
        self.salary = 200

    def __str__(self) -> str:
        return Manager.__str__
    
    def manageSimple(self):
        print("do this task")

class Simple(Worker):

    def __init__(self,age,name,sex) -> None:
        super().__init__(age,name,sex)
        self.salary = 50
    
    def __str__(self) -> str:
        return super().__str__

    def complain(self):
        print("i want a break")

if __name__ == "__main__":
    St1 = Student(19, "Sasha", "Female", 89, "First")
    M1 = Manager(22, "Michael", "Male")
    Si1 = Simple(18, "Kevin", "Male")
    bunch = [St1,M1,Si1]
    print(Si1)
    for x in bunch:
        if issubclass(type(x),Simple):
            x.complain()
        if issubclass(type(x),Student):
            x.study()
        if issubclass(type(x),Manager):       
            x.manageSimple()