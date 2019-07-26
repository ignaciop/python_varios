initial_inv = float(input('Initial investment: '))
interest_rate = float(input('Interest rate (in percent): '))
years = float(input('Number of years of investment: '))


CI = initial_inv * (pow((1 + interest_rate / 100), years))
CI2 = initial_inv * (pow((1 + (interest_rate / 100) / 12), years * 12))
CI3 = initial_inv * (pow((1 + (interest_rate / 100) / 365.24), years * 365.24))


print("Annually: ${0:0.2f}".format(CI))
print("Monthly: ${0:0.2f}".format(CI2))
print("Daily: ${0:0.2f}".format(CI3))