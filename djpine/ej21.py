g = 9.8
h0 = 1.6
v0 = 14.2

t = 0.5
h = h0 + v0*t - 0.5*g*t**2
v = v0 - g*t

print(h)
print(v)

t = 2.0
h = h0 + v0*t - 0.5*g*t**2
v = v0 - g*t

print(h)
print(v)
