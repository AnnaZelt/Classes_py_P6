class Lion:
    sex = ""
    age = 0
    
    def __init__(self,sex,age) -> None:
        self.sex = sex
        self.age = age

    def __str__(self) -> str:
        return f"Sex: {self.sex}, Age: {self.age}"
    
    def hunt(self):
        pass

    def sleep(self):
        pass

class Fish:
    sex = ""
    age = 0

    def __init__(self,sex,age) -> None:
        self.sex = sex
        self.age = age

    def __str__(self) -> str:
        return f"Sex: {self.sex}, Age: {self.age}"

    def move(self):
        pass

    def sleep(self):
        pass

if __name__ == "__main__":
    L1 = Lion("Male", 14)
    print(L1)