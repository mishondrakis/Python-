numbers = [2,4,2,4,4, 4, 4, 4 , 5, 5 ,6 , 6  ]
unique = [23,42,42,23,131,313,133,33,3,3,3,3,3]

for number in numbers:
    if number not in unique:
        unique.append(number)

print(unique)


removeDuplicate = []

for number in numbers:
    if number not in removeDuplicate:
        removeDuplicate.append(number)

print(removeDuplicate)