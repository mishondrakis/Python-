class Vihicle:
    def __init__(self,color,manuf):
        self.color = color
        self.manuf = manuf
        self.gas = 4

    def drive(self):
        if self.gas > 0:
            self.gas -= 1
            print("The {} {} goes Vroomm".format(self.color,self.manuf))
        else:
            print("The {} {} sputters out of gas".format(self.color,self.manuf))


class Car(Vihicle):
    def radio(self):
        print("Classic mussic ON")

    def window(self):
        print("window is down")

class Motorcycle(Vihicle):
    def helmet(self):
        print("Put on the helmet")

my_car = Car('silver','mercedes')

print(my_car.drive())
print(my_car.drive())
print(my_car.drive())
print(my_car.drive())
print(my_car.drive())