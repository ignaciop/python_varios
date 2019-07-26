from math import floor

months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 
            'May': 5, 'June': 6, 'July': 7, 'August': 8, 
                'September': 9, 'October': 10, 'November': 11, 
                    'December': 12}
                    
month = input('Month: ')
day = int(input('Day: '))
year = int(input('Year: '))

t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
year -= months[month] < 3
wd = floor((year + year / 4 - year / 100 +  year / 400 +
        t[months[month] - 1] + day) % 7)
        
if wd == 1:
    print('Monday')
elif wd == 2:
    print('Tuesday')
elif wd == 3:
    print('Wednesday')
elif wd == 4:
    print('Thursday')
elif wd == 5:
    print('Friday')
elif wd == 6 or wd == 0:
    print('Saturday')
else:
    print('Sunday')

