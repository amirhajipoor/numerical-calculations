import math

MAX_ITER = 20
LIMIT = 1e-12

def f(x):
    return pow(math.e, x) - 3 * (pow(x, 2))

def regula_falsi(a, b, f):
    i = 0
    fa = f(a)
    fb = f(b)

    if fa == 0:
        return a, 0
    if fb == 0:
        return b, 0
    if fa * fb > 0:
        raise RuntimeError("Root can not be calculated")

    c = find_c_point(f, a, b)
    fc = f(c)

    while abs(fc) > LIMIT and i < MAX_ITER:
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c = find_c_point(f, a, b)
        fc = f(c)
        i += 1

    return c, i

def find_c_point(f, a, b):
    fa = f(a)
    fb = f(b)
    denom = (fb - fa)
    if denom == 0:
        raise ZeroDivisionError("f(a) and f(b) are equal; interpolation is impossible")
    return - fa * ((b - a) / denom) + a

root, iter = regula_falsi(0, 1, f)
print("Root: {0}, Iter: {1}".format(root, iter))
