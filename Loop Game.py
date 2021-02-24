i = 1

while i <= 5:
    print("Misho" * i)
    i += 1

secretNumber = 9
guessLimit = 3
guessCountBoss = 0
counter = 3
while guessCountBoss < guessLimit:
    guessNumber = int(input(f'Please provide a number, you have {counter}'))
    guessCountBoss += 1
    counter -= 1
    if guessNumber == secretNumber:
        print(f"Good job, you won, the number is {secretNumber}")
        break

else:
    print("I'm sorry, you lost!")

