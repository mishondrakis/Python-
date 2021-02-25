
cheese = 'chedar'

def mix_ingredients():
    print("mix ingredients")
    print("add water")
    print("add sugar")

def cooking_pancake():
    mix_ingredients()
    global cheese
    cheese = 'swiss'
    print("add more sugar")
    pancake = "this is fantastic {} omlete".format(cheese)
    return pancake

def cooking_sausage():
    mix_ingredients()
    print("add oil please")
    sausage = "this is fantastic sausage with {}".format(cheese)
    return sausage
print(cooking_pancake())
print(cooking_sausage())