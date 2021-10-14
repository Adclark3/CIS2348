# Avery Clark
# 1907691

from datetime import date

months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
          'September': 9, 'October': 10, 'November': 11, 'December': 12}

data_file = open('inputDates.txt', 'r')
today = date.today()
current_year = today.strftime('%Y')
new_dates = open('parsedDates.txt', 'w')
while date != '-1':
    date = data_file.readline()

    if date.__contains__(",") and not date.__contains__('.'):
        data = date.split()
        month = months[data[0]]
        day = data[1]
        day = day.replace(',', "")
        year = data[2]

        if current_year >= year:
            new_dates.write('{}/{}/{}\n'.format(month, day, year))
