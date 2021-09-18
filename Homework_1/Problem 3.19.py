# Avery Clark
# 1907691
import math

print('Enter wall height (feet):')
height = int(input())
print('Enter wall width (feet):')
width = int(input())
area = width * height
print('Wall area:', area, 'square feet')

gal_needed = area / 350
print('Paint needed:', '{:.2f}'.format(gal_needed), 'gallons')

cans = math.ceil(gal_needed)
print('Cans needed:', cans, 'can(s)\n')

paint_colors = {'red': 35, 'blue': 25, 'green': 23}

cost = cans * 23
print('Choose a color to paint the wall:')
color = input()
paint_cost = paint_colors[color] * cans
print('Cost of purchasing', color, 'paint: $', end='')
print(paint_cost)
