class Pet:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"I am {self.name} and I am {self.age} years old.")

class Cat(Pet):

    def speak(self):
        print("Meow")


class Dog(Pet):

    def __init__(self, name, age,color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print("Aww")

    def introduce(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}.")

class Fish(Pet):

    def speak(self):
        pass

d = Dog("Rex",14,"blue")
d.introduce()
