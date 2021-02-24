command = ""
isCarOn = False
isCarStopped = False
while True:
    command = input("> ").lower()

    if command == "start":
        if isCarOn:
            print("The car is already started")
        else:
            isCarOn = True
            isCarStopped = False
            print("The car is started")
    elif command == "stop":
        if not isCarOn:
            print("the car is already stopped")
        else:
            isCarOn = False
            print("The car stopped")
    elif command == "help":
        print(""" 
start - to start the car
stop  - to stop the car
quit  - to quit
        """)
    elif command == "quit":
        break
    else:
        print("I'm sorry, I don't understand this, please type help for more options ")