numbers = {
    "Y": "She is a bad girl, be carefull",
    "o": "is a",
    "a": "bad",
    "n": "girl be carefull",

}

name = input("Girl: ")

output = ""

for ch in name:
    output += numbers.get(ch, "! ") + " "

print(output)
