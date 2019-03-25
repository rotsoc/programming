from math import *

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


if __name__ == "__main__":
    main()
