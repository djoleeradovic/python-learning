class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")
    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):
    def run(self):
        print("Rabbit is running")
class Fish(Animal):
    def swim(self):
        print("Fish is swiming")
class Hawk(Animal):
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed
        print(f"I am hawk my name is {self.name} and i fly speed {self.speed} ")
Hawk("Pera",14).eat()
