from math import *
from matplotlib import pyplot as plt

def main():
    x0 = 2.3
    def f(x):
        return x**2 + 0.25*x - 5
    TOL = 1e-12
    if abs(f(x0)-0.0) < TOL:
        print(f"x0 = {x0} is a zero of the function.")
    else:
        print(f"x0 = {x0} is not a zero of the function.")

    L = [k/99 for k in range(0, 100)]
    print(f"The list of 100 equidistant point is {L} and its length is {len(L)}")

    xplot = [k/99 for k in range(0, 100)]

    yplot = []

    for x in xplot:
        yplot.append(atan(x))

    print(f"The xplot is {xplot}")
    print(f"The yplot is {yplot}")

    s = sum(1/sqrt(i) for i in range(1, 201))

    print(f"The sum is {s}")

    a = -0.5
    h = 1/1000
    u = [exp(0), exp(h*a), exp(2*h*a)]

    for n in range(3, 1001):
        u.append(u[n-1]+h*a*((23/12)*u[n-1]-(4/3)*u[n-2]+(5/12)*u[n-3]))

    print(f"u is {u}")

    td = [n*h for n in range(0, 1001)]

    print(f"time is {td}")

    plt.plot(u, td, 'd')

    yplot = [exp(a*tt) for tt in td]

    plt.plot(yplot, td)

    plt.show()
    


if __name__ == "__main__":
    main()
