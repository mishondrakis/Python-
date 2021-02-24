try:
    age = int(input("Age: "))
    print(age)

except ValueError:
    print("Please provide a number")
except ZeroDivisionError:
    print("age can't be 0 ")
