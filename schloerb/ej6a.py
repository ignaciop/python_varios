def rectangle(f, a, b, n):
    width = (b - a) / n
    s = 0
    
    for i in range(n):
        height = f(a + i * width)
        area = width * height
        s += area

    return s

def trapezoidal(f, a, b, n):
    width = (b - a) / n
    s = 0
    
    for i in range(1, n):
        s += f(a + i*width)

    return width*((f(a) + f(b)) / 2 + s)

def simpson(f, a, b, n = 50):
    h = (b - a) / n
    k = 0.0
    x = a + h

    for i in range(1, int(n / 2 + 1)):
        k += 4 * f(x)
        x += 2 * h

    x = a + 2 * h

    for i in range(1, int(n / 2)):
        k += 2 * f(x)
        x += 2 * h

    return (h / 3) * (f(a) + f(b) + k)