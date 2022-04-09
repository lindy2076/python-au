from numpy import zeros
from numba import jit, int32

@jit(nopython=True)
def generate_table(num: int, size: int):  # генерация самой таблицы из строки
    new_table = zeros((size, size), dtype=int32)
    c, r = size - 1, size - 1
    while num:
        new_table[r][c] = num % size
        if not c:
            c = size
            r -= 1
        c -= 1
        num //= size
    return new_table


@jit(nopython=True)
def associative_test(table, n: int) -> bool:
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if table[table[x][y]][z] != table[x][table[y][z]]:
                    return 0
    return 1


def associative_test_optimized(table: list[list], n: int) -> bool:
    
    return 1


@jit(nopython=True)
def count(k):
    c = 0
    i = 0
    m = k**(k*k)
    while i < m:
        c += associative_test(generate_table(i, k), k)
        i += 1
    return c


def main():
    k = int(input())

    print(count(k))


if __name__ == "__main__":
    main()
