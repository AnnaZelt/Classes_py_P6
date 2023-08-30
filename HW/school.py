from enum import Enum
import pandas as pd

class Actions(Enum):
    PRINT_ALL = 0
    PRINT_AVG = 1
    PRINT_HIGHEST = 2
    PRINT_LOWEST = 3
    ADD = 4
    EXIT = 5

class Student:
    def __init__(self,Name,Age,Sex,Grades) -> None:
        self.Name = Name
        self.Age = Age
        self.Sex = Sex
        self.Grades = Grades
    
    def __str__(self) -> str:
        return f"Name: {self.Name}, Age: {self.Age}, Sex: {self.Sex}, Grades: {self.Grades}"
    
    def printAvg(self):
        total_sum = 0
        num_grades = len(self.Grades)
        for grade_dict in self.Grades:
            for grade in grade_dict.values():
                total_sum += int(grade)
        average = total_sum / num_grades
        print(f"Average grade for {self.Name}: {average:.2f}") 
    
    def grade(self):
        total_sum = 0
        num_grades = len(self.Grades)
        for grade_dict in self.Grades:
            for grade in grade_dict.values():
                total_sum += int(grade)
        average = total_sum / num_grades
        return average
        
class Tests:
    def __init__(self, test_list) -> list:
        self.Grades = []
        for subject, grade in test_list:
            self.Grades.append({subject: grade})
            
# test_list = [("Math", 89), ("Physics", 81), ("Literature", 93), ("P.E", 78)]
# G1 = Tests(test_list)
# S1 = Student("Alex", 13, "Female", G1.tests)
# students = [S1]
    
def displayMenuActions():
    for x in Actions: print(f"{x.value} - {x.name}")
    return Actions(int(input("Select an action: ")))

def main():
    global students
    while(True):
        selection = displayMenuActions()
        if selection == Actions.PRINT_ALL: 
            printAll()
        if selection == Actions.PRINT_AVG:
            for x in students:
                x.printAvg()
        if selection == Actions.PRINT_HIGHEST:
            highest = 0
            for x in students:
                if x.grade() > highest:
                    highest = x.grade()
            print (highest)
        if selection == Actions.PRINT_LOWEST:
            lowest = 100
            for x in students:
                if x.grade() < lowest:
                    lowest = x.grade()
            print(lowest)       
        if selection == Actions.ADD:
            add()
        if selection == Actions.EXIT:
            save()
            return

def printAll():
    global students
    for x in students:
        print(x)

def add():
    global students
    name = input("Enter name: ")
    age = input("Enter age: ")
    sex = input("Enter sex: ")
    print("Enter grades: ")
    tests = [("Math", input("Math: ")), ("Physics", input("Physics: ")), ("Literature", input("Literature: ")), ("P.E", input("P.E: "))]
    grades = Tests(tests)
    student = Student(name,age,sex,grades.Grades)
    students.append(student)

def printHighest():
        global students
        highest_grade = 0
        total_sum = 0
        for student in students:
            currenStudent = student
            for grade_dict in students[-1]:
                for grade in grade_dict.values():
                    total_sum += int(grade)
            average = total_sum / 4
            if average > highest_grade:
                print(currenStudent)
                return

def save():
    global students
    student_data = []
    for x in students:
        student_data.append(vars(x))
    
    df = pd.DataFrame(student_data)
    df.to_json('students.json', orient='records')

def load():
    global students
    try:
        df = pd.read_json('students.json')
    except FileNotFoundError:
        print("Creating an empty students.json file.")
        with open('students.json', 'w') as f:
            f.write('[]')  # Write an empty JSON array
        return
    students = []
    for _, row in df.iterrows():
        student = Student(**row)
        students.append(student)

if __name__ == "__main__":
    load()
    main()
