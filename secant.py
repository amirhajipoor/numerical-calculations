import math

MAX_ITER = 20
LIMIT = 1e-12

def f(x):
    return pow(math.e, x) - 3 * (pow(x, 2))

def secant(a, b, f):
    fa = f(a)
    fb = f(b)

    if fa == 0:
        return a, 0
    if fb == 0:
        return b, 0

    c = b
    for i in range(1, MAX_ITER + 1):
        denom = (fb - fa)
        if denom == 0:
            raise ZeroDivisionError("Division by zero: f(b) - f(a) == 0")

        c = b - fb * ((b - a) / denom)
        fc = f(c)

        if abs(fc) <= LIMIT or abs(c - b) <= LIMIT:
            return c, i

        a, fa = b, fb
        b, fb = c, fc

    return c, MAX_ITER

root, iters = secant(0, 1, f)
print("Root: {0}, Iter: {1}".format(root, iters))
