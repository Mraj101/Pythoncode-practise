class Animals:
    animalType="Mammal"

class Pets(Animals):
    color= "white"

class Dog:
    @staticmethod
    def bark():
        print("BOw bow")

d=Dog()
d.bark()