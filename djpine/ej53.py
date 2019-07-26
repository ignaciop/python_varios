x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

last_column_x = [x[-1] for x in x]
print(last_column_x)

tsquare_middle_column = [2*x[1]**2 for x in x]
print(tsquare_middle_column)