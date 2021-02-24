
numbers = [5, 3, 4, 43, 4, 3, 4, 3, 5, 56]

numbers.sort()
print(numbers)
goodNumbers = []

for num in numbers:
    if num not in goodNumbers:
        goodNumbers.append(num)


print(goodNumbers)