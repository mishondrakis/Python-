numbers = [5, 2, 5, 2, 2, 8, 9 ,11, 12, 212, 11111, 22212,2,1, 0]

for x in numbers:
    output = ''

    for count in range(x):
        output += 'x'

    print(output)


names = ['Mihail', 'John', "Maria", "Iskam", 'I love your']

names[0] = 'Mihail Hadzhiev'
print(names)

maxNumber = 0

for number in numbers:
    if maxNumber < number:
        maxNumber = number

print(maxNumber)
