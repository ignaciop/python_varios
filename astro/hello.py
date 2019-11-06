from datetime import datetime as dt

fn = input('First name: ')
ln = input('Last name: ')
by = int(input('Birth year: '))

current_year = dt.now().year
age = current_year - by

print('Hello World, my name is {0} {1}, I am {2} years old, and I wrote this Python code!!'
        .format(fn, ln, age))