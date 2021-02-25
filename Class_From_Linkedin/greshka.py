
def mix_cooking():
    print("We mix our ingredients")
    print("after that we put oil")
    print("ingredients are very important")


def cooking_pancakes(*ingredients):
    mix_cooking()
    print("add sugar")
    print("add chocolate")
    pancakes = "these are fantastic pancakes with ingredients {} ".format(len(ingredients))
    return pancakes

def cooking_sasusage(*ingredients):
    mix_cooking()
    print("add oil")
    sausage = "this is very good sausage".format(len(ingredients))
    return sausage

print(cooking_sasusage('becan'))


