
rowCars = ['Ford', 'Ferrari', "Nissan", 'Toyota']

print(rowCars[0])
rowCars[1] = 'Iskam'
print(rowCars[1])
print(rowCars)
rowCars.append('Honda')
print(rowCars)
rowCars.remove("Nissan")
if 'Nissan' in rowCars:
    rowCars.remove('Nissan')

print(rowCars)
rowCars.sort()
print(rowCars)

rowCars.insert(1,'Tesla')
print(rowCars.index('Tesla'))
rowCars.pop(1)
print(rowCars)
