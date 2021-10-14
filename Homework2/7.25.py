# Avery Clark
# 1907691

def exact_change(input_val):

    num_dollars = 0
    num_quarters = 0
    num_dimes = 0
    num_nickles = 0
    num_pennies = 0

    if input_val <= 0:

        print('no change')

    else:

        num_dollars = input_val // 100
        input_val %= 100

        num_quarters = input_val // 25
        input_val %= 25

        num_dimes = input_val // 10
        input_val %= 10

        num_nickles = input_val // 5
        input_val %= 5

        num_pennies = input_val

    return num_dollars, num_quarters, num_dimes, num_nickles, num_pennies


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if num_dollars > 1:
        print('%d dollars' % num_dollars)
    elif num_dollars == 1:
        print('%d dollar' % num_dollars)

    if num_quarters > 1:
        print('%d quarters' % num_quarters)
    elif num_quarters == 1:
        print('%d quarter' % num_quarters)

    if num_dimes > 1:
        print('%d dimes' % num_dimes)
    elif num_dimes == 1:
        print('%d dime' % num_dimes)

    if num_nickels > 1:
        print('%d nickels' % num_nickels)
    elif num_nickels == 1:
        print('%d nickel' % num_nickels)

    if num_pennies > 1:
        print('%d pennies' % num_pennies)
    elif num_pennies == 1:
        print('%d penny' % num_pennies)
