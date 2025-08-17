import math

STOP_LIMIT = 1e-12

def f(x):
    return pow(math.e, x) - 3 * (pow(x, 2))

def g(x):
    return math.log(3) + 2 * math.log(x)

def fixed_point_method(x0):
    i = 0

    while abs(f(x0)) > STOP_LIMIT:
        x1 = g(x0)
        x0 = x1
        i += 1
    return x0, i

root, iter = fixed_point_method(3.2)
print("Root: {0}, Iter: {1}".format(root, iter))
