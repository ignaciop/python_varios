import numpy as np

money = float(input('How much money (in dollars) in your lunch account? '))
day = int(input('What day of the month is today? '))
dim = int(input('How many days in this month? ' ))

days_left = dim - day + 1
total = money/days_left

print('You can spend ${0:0.2f} each day for the rest of the month.'
        .format(total))

# With dictionaries

mad = {'jan': 31, 'feb': 28, 'mar': 31, 'abr': 30, 'may': 31, 
        'jun': 30, 'jul': 31, 'aug': 31, 'sep': 30, 'oct': 31, 
        'nov': 30, 'dic': 31}
money = float(input('How much money (in dollars) in your lunch account? '))
day = int(input('What day of the month is today? '))
month = input('Month? ' )

days_left = mad[month] - day + 1
total = money/days_left

print('You can spend ${0:0.2f} each day for the rest of the month.'
        .format(total))

