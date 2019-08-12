import vpython as vp

L = 1
R = 0.3

for i in range(-L, L + 1):
    for j in range(-L, L + 1):
        for k in range(-L, L + 1):
            if (i + j + k) % 2 != 0:
                vp.sphere(pos = vp.vector(i, j, k), color = vp.color.green,
                            radius = R)