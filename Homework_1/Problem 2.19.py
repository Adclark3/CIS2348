# Avery Clark
# 1907691

print('Enter amount of lemon juice (in cups):')
lemon = float(input())
print('Enter amount of water (in cups):')
water = float(input())
print('Enter amount of agave nectar (in cups):')
nectar = float(input())
print('How many servings does this make?\n')
servings = float(input())

print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(lemon), 'cup(s) lemon juice')
print('{:.2f}'.format(water), 'cup(s) water')
print('{:.2f}'.format(nectar), 'cup(s) agave nectar\n')


print('How many servings would you like to make?')
num_served = float(input('\n'))

yields = num_served / servings
print('Lemonade ingredients - yields', '{:.2f}'.format(num_served), 'servings')
lemon_amount = lemon * yields
print('{:.2f}'.format(lemon_amount), 'cup(s) lemon juice')
water_amount = water * yields
print('{:.2f}'.format(water_amount), 'cup(s) water')
nectar_amount = nectar * yields
print('{:.2f}'.format(nectar_amount), 'cup(s) agave nectar\n')

print('Lemonade ingredients - yields', '{:.2f}'.format(num_served), 'servings')
lemon_gal = lemon_amount / 16
print('{:.2f}'.format(lemon_gal), 'gallon(s) lemon juice')
water_gal = water_amount / 16
print('{:.2f}'.format(water_gal), 'gallon(s) water')
nectar_gal = nectar_amount / 16
print('{:.2f}'.format(nectar_gal), 'gallon(s) agave nectar')
