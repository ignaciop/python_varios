import matplotlib.pyplot as plt
from scipy.constants import golden

f, r = [], []
f0 = 0
f1 = 1

f.append(f0)
f.append(f1)


while (1):

    t = f1
    f1 = f1 + f0
    f0 = t

    f.append(f1)
    r.append(f1/f0)

    if abs(golden - f1/f0) <= 1e-6:
        break


print('Fibonacci numbers: ', f)
print('Ratios of successive numbers: ', r)
print('Number of iterations before successive iterations don\'t change by more than 1e-6: ', len(r))


plt.figure()
plt.plot(r, '.', label = 'Ratios')
plt.plot([golden for g in range(0, len(r))], '-', zorder = -1, label = 'Golden ratio')
plt.xlabel('Number of iterations')
plt.ylabel('Ratio')
plt.grid()
plt.tight_layout()
plt.legend(loc = 'best')
plt.show()