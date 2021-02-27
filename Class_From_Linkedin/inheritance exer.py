class Vihicle:
    def __init__(self, color, year, brand):
        self.color = color
        self.year = year
        self.brand = brand
        self.gas = 4
        self.windShieldJuice = 20

    def drive(self):
        if self.gas > 0 and self.windShieldJuice > 1:
            self.gas -= 1
            self.gas -= 3
            print("let's goooo The {} car {} wow  brmmmmmmm {} cool "
                  .format(self.color, self.year, self.brand))
        else:
            print("We are out of juice noooooo")


class Car(Vihicle):
    def window(self):
        print("window goes down")

    def radio(self):
        print("radio is on,... yeee ")

class Motorcycle(Vihicle):
    def driveLikeCrazy(self):
        print("You man, are crazy! ")


fun = Car('black',2020,"mercedes")
print(fun.radio())