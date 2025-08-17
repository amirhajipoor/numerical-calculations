import math

LIMIT = 1e-7

def f(x):
    return (math.e ** x) - 3 * (x ** 2)

def bisection(a, b, f, tol=LIMIT, max_iter=1000, use_residual=True):
    fa = f(a)
    fb = f(b)

    if fa == 0:
        return a, 0
    if fb == 0:
        return b, 0

    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs (a bracket is required).")

    it = 0
    while it < max_iter:
        c = (a + b) / 2.0
        fc = f(c)

        if use_residual:
            if abs(fc) <= tol:
                return c, it + 1
        else:
            if (b - a) / 2.0 <= tol:
                return c, it + 1

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        it += 1

    raise RuntimeError(f"Max iterations ({max_iter}) reached. Last midpoint {c} with f(c)={fc}")

root, iters = bisection(0, 1, f, tol=1e-4, use_residual=True)
print("root:", root, "iters:", iters)
