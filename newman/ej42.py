import numpy as np

def rc(a, b, c):
    disc = b**2 - 4*a*c
    x1 = (-b + np.sqrt(disc))/(2*a)
    x2 = (-b - np.sqrt(disc))/(2*a)
    
    x1b = 2*c/(-b - np.sqrt(disc))
    x2b = 2*c/(-b + np.sqrt(disc))
    
    return x1, x2, x1b, x2b
    
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

x1, x2, x1b, x2b = rc(a, b, c)
print(x1, x2)
print(x1b, x2b)

def rc_correct(a, b, c):
    disc = b**2 - 4*a*c
    
    if disc <= 0:
        x1 = 2*c/(-b - complex(0, np.sqrt(np.abs(disc))))
        x2 = 2*c/(-b + complex(0, np.sqrt(np.abs(disc))))
    else:
        x1 = 2*c/(-b - np.sqrt(disc))
        x2 = 2*c/(-b + np.sqrt(disc))
        
    return x1, x2
    
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

x1, x2 = rc_correct(a, b, c)

print(x1, x2)