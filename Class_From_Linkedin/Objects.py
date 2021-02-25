class jeans:
    def __init__(self, waist, length, color):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False

    def put_on(self):
        print('Putting on {}x{} {} jeans'.format(self.waist, self.length, self.color))
        self.wearing = True

    def take_off(self):
        print('Taking off {}x{} {} jeans.'.format(self.waist, self.length, self.color))
        self.wearing = False


# print(type(jeans))
# print(dir(jeans))
my_jeans = jeans(31, 32, 'Blue')
print(my_jeans.put_on())
print(my_jeans.wearing)
print(my_jeans.take_off())
print(my_jeans.wearing)
