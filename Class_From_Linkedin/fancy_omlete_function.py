
def mix_cooking():
    print("mixing ingredients")
    print("baking the ingredients")
    print("mixing again the ingredients")

def baking_pancakes(ingredient):
    mix_cooking()
    omlete = "this omlet with ingredient {} is awesome".format(ingredient)
    return omlete

def baking_sausages(ingredient):
    mix_cooking()
    sausage = "this sausage with this ingredient {} is awesome".format(ingredient)
    return sausage

def fancy_omlete(*ingredients):
    mix_cooking()
    fancy_omlete = "this is fantastic fancy omlete with ingredients {} ".format(len(ingredients))
    return fancy_omlete

print(fancy_omlete('bekon','dwdw'))