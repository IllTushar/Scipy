from scipy.integrate import quad, dblquad, nquad
import math


def f(x: float):
    return math.sin(x)


def double_integration(x, y):
    return x ** 2 + y ** 2


def n_integration(x, y):
    return x * y


if __name__ == '__main__':
    result, error = quad(f, 0, math.pi / 2)
    # print(result)
    # print(error)

    result1, error1 = dblquad(double_integration, -5, 5, -2, 2)
    # print(result1)
    # print(error1)

    result2, error2 = nquad(n_integration,[ [-4, 4], [-1, 5]])
    print(result2)
    print(error2)
