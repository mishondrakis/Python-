class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):

        print("Talk")


John = Person("John smith")
print(John.name)
John.talk()


class Dog:
    def __init__(self,poroda):
        self.poroda = poroda

    def baybay(self):
        print("Bay bay")


dog = Dog("pincher")
print(dog.poroda)
dog.baybay()