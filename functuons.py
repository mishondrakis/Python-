def mishoIskam(firstName, lastName):
    print(f"{firstName} {lastName} wants to learn Python")


mishoIskam("Mihail", "Hadzhiev®")


def square(number):
    return number * number


result = square(5)

print(result)

message = input(">")


def emoji_converter(message):
    words = message.split(" ")
    emojix = {
        ":)": "🥰",
        ";(": "🥵"
    }

    otput = ""
    for word in words:
        otput += emojix.get(word, word) + " "

    return print(otput)


emoji_converter(message)


