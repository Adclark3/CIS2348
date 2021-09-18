# Avery Clark
# 1907691

print('Birthday Calculator')

print('Current day')
cur_month = int(input('Month:'))
cur_day = int(input('Day:'))
cur_year = int(input('Year:'))

print('Birthday')
bir_month = int(input('Month:'))
bir_day = int(input('day:'))
bir_year = int(input('Year:'))

age = cur_year - bir_year
if (bir_month == cur_month) and (bir_day > cur_day):
    age -= 1
if bir_month > cur_month:
    age -= 1
if (bir_month == cur_month) and (cur_day == bir_day):
    print("Happy Birthday")

print('You are', age, 'years old')
