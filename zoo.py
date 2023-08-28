from enum import Enum
import pickle
import pandas as pd
import os

class Actions(Enum):
    PRINT_ALL = 0
    PRINT_NON_PREDATORS = 1
    PRINT_PREDATORS = 2
    ADD = 3
    EXIT = 4

class Animals(Enum):
    FISH = 0
    TURTLE = 1
    LION = 2
    TIGER = 3

class Animal:
    def __init__(self,age,name,sex) -> None:
        self.age = age
        self.name = name
        self.sex = sex
    
    def __str__(self) -> str:
        return f"Age: {self.age}, Name: {self.name}, Sex: {self.sex}"
    
    def move(self):
        print("move animal")

    def eat(self):
        print("eat animal")
    
class Predator(Animal):
    def __init__(self, age, name, sex, habitat) -> None:
        super().__init__(age, name, sex)
        self.habitat = habitat
    
    def __str__(self) -> str:
        return (super().__str__()+ f", Habitat: {self.habitat}")
    
    def move(self):
        print("move predator")

    def eat(self):
        print("eat predator")

class Fish(Animal):
    def __init__(self, age, name, sex, habitat) -> None:
        super().__init__(age, name, sex)
        self.habitat = habitat
    
    def __str__(self) -> str:
        return (super().__str__()+ f", Habitat: {self.habitat}")
    
    def move(self):
        print("fish swim")

    def eat(self):
        print("eat fish")
    
class Turtle(Animal):
    def __init__(self, age, name, sex, habitat) -> None:
        super().__init__(age, name, sex)
        self.habitat = habitat
    
    def __str__(self) -> str:
        return (super().__str__()+ f", Habitat: {self.habitat}")
    
    def move(self):
        print("turtle swim")

    def eat(self):
        print("eat turtle")
    
class Lion(Predator):
    def __init__(self, age, name, sex, habitat, huntMethod) -> None:
        super().__init__(age, name, sex, habitat)
        self.huntMethod = huntMethod

    def __str__(self) -> str:
         return (super().__str__()+ f", Hunting method: {self.huntMethod}")
        
    def move(self):
        print("chase lion")

    def eat(self):
        print("eat lion")

class Tiger(Predator):
    def __init__(self, age, name, sex, habitat, huntMethod) -> None:
        super().__init__(age, name, sex, habitat)
        self.huntMethod = huntMethod

    def __str__(self) -> str:
         return (super().__str__()+ f", Hunting method: {self.huntMethod}")
        
    def move(self):
        print("stalk tiger")

    def eat(self):
        print("eat tiger")

F1 = Fish(8, "John", "Male", "Aquatic")
F2 = Fish(9, "Brienne", "Female", "Aquatic")
Tu1 = Turtle(11, "Johnathan", "Male", "Aquatic")
Tu2 = Turtle(12, "Brian", "Male", "Aquatic")
L1 = Lion(4, "Simba", "Male", "Terrestrial", "Chasing")
L2 = Lion(1, "Loren", "Female", "Terrestrial", "Chasing")
Ti1 = Lion(3, "Maxine", "Female", "Terrestrial", "Stalking")
Ti2 = Lion(6, "Selune", "Female", "Terrestrial", "Stalking")
animals = [F1,F2,Tu1,Tu2,L1,L2,Ti1,Ti2]
    
def displayMenuActions():
    for x in Actions: print(f"{x.value} - {x.name}")
    return Actions(int(input("Select an action: ")))

def displayMenuAnimals():
    for x in Animals: print(f"{x.value} - {x.name}")
    return Animals(int(input("Select an animal to add: ")))

def main():
    global animals
    while(True):
        selection = displayMenuActions()
        if selection == Actions.PRINT_ALL: 
            printAll()
        if selection == Actions.PRINT_NON_PREDATORS:
            for x in animals:
                if not (issubclass(type(x), Predator)):
                    if (issubclass(type(x),Fish)):
                        print(f"Fish: {x}")
                    if (issubclass(type(x),Turtle)):
                        print(f"Turtle: {x}")
        if selection == Actions.PRINT_PREDATORS:
            for x in animals:
                if (issubclass(type(x), Predator)):
                    if (issubclass(type(x),Lion)):
                        print(f"Lion: {x}")
                    if (issubclass(type(x),Tiger)):
                        print(f"Tiger: {x}")
        if selection == Actions.ADD:
            add()
        if selection == Actions.EXIT:
            saveP()
            return

def printAll():
    for animal in animals:
        print(animal)

def add():
    global animals
    selection = displayMenuAnimals()
    if selection == Animals.FISH:
        animal = Fish(input("Enter age: "),input("Enter name: "),input("Enter sex: "),input("Enter habitat: "))
        animals.append(animal)
    if selection == Animals.TURTLE:
        animal = Turtle(input("Enter age: "),input("Enter name: "),input("Enter sex: "),input("Enter habitat: "))
        animals.append(animal)
    if selection == Animals.LION:
        animal = Lion(input("Enter age: "),input("Enter name: "),input("Enter sex: "),input("Enter habitat: "),input("Enter hunting method: "))
        animals.append(animal)
    if selection == Animals.TIGER:
        animal = Tiger(input("Enter age: "),input("Enter name: "),input("Enter sex: "),input("Enter habitat: "),input("Enter hunting method: "))
        animals.append(animal)

def save():
    global animals
    animal_data = []
    for animal in animals:
        animal_data.append(vars(animal))
    
    df = pd.DataFrame(animal_data)
    df.to_json('animals.json', orient='records')


def load():
    global animals
    df = pd.read_json('animals.json')
    
    animals = []
    for _, row in df.iterrows():
        animal_class = globals()[row['__class__']]
        animal = animal_class(**row.drop('__class__').to_dict())
        animals.append(animal)

def saveP():
    global animals
    with open('animals.pkl', 'wb') as pickle_file:
        pickle.dump(animals, pickle_file)

def loadP():
    global animals
    if os.path.exists('animals.pkl') and os.path.getsize('animals.pkl') > 0:
        with open('animals.pkl', 'rb') as pickle_file:
            animals = pickle.load(pickle_file)
    else:
        print("No valid pickled data found. Starting with an empty list of animals.")
        animals = []

if __name__ == "__main__":
    loadP()
    main()