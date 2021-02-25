def mix_cocking():
    print("Mixing ingredients")
    print("mixing everything")




def cooking_sausage(ingredient): #ingredient e parameter
    mix_cocking()
    sausage = "this a {} sausage is very good".format(ingredient)
    return sausage


def cooking_pancake(ingredient):
    mix_cocking()
    pancake = "this is a {} pancake mmmm ".format(ingredient)
    return pancake


print(cooking_pancake("bekon")) #becon is an argument
