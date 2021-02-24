is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day, drink plenty of water Mihail ")

elif is_cold:
    print("It's very cold, be careful ! ")
else:
    print("It's cold stay home")


priceHouse = 100000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * priceHouse
else:
    down_payment = 0.2 * priceHouse
print(f'Down payment for the house is: ${down_payment}')


has_money = True
has_perfect_credit = True

if has_money and not has_perfect_credit:
    print('Awesome you are rich')
else:
    print('Sorry no money for you :( ')
