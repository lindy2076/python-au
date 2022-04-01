import multiprocessing
import time
from random import uniform


def f(x: float) -> float:
    return 3 * ((x**3 + 2*x) ** (1/2)) - 1.2 * (x*x)


def under_f(x: float, y: float) -> int:
    return 1 if f(x) >= y else 0


def monte_carlo_int_usual(a: float, b: float, pool, n: int) -> float:
    res = sum(pool.map(f, [uniform(a, b) for _ in range(n)])) / n
    return res * (b - a)


def monte_carlo_int_geom(a: float, b: float, pool, n: int) -> float:
    ymax = 10
    k = sum(pool.starmap(under_f, zip([uniform(a, b) for _ in range(n)], [uniform(0, ymax) for _ in range(n)])))
    return (b - a) * (ymax - 0) * (k / n)


def main():
    print("This program calculates an integral of 3sqrt(x^3 + 2x) - 1.2x^2 from 0 to 1")
    print("enter n please...\n:|", end="")
    try:
        n = int(input())
    except ValueError:
        print("i need an integer...")
    except Exception as wtf:
        print("???" + str(wtf.__class__))
    else:
        print("expected result: 2.71093602826832.")
        pool = multiprocessing.Pool()
        t0 = time.time()
        print("Traditional method result: ", monte_carlo_int_usual(0, 1, pool, n))
        print("Time spent:", time.time() - t0)

        t0 = time.time()
        print("Geom method result:", monte_carlo_int_geom(0, 1, pool, n))
        print("Time spent:", time.time() - t0)


if __name__ == "__main__":
    main()
else:
    print("process", end=" ")
