from numba import jit
from numpy import array

@jit(nopython=True, fastmath=True)
def to_system(num: int, base: int):  # генерация строки таблицы
    if num == 0:
        res = '0'
    else:
        res = str(num % base)
        num //= base
    while num > 0:
        res = str(num % base) + '.' + res
        num //= base
    while len(res.split('.')) < base*base:
        res = str(0) + '.' + res
    return res


def generate_table(num: int, size: int) -> list[list]:  # генерация самой таблицы из строки
    string = to_system(num, size)
    new_table = array([[0 for _ in range(size)] for _ in range(size)])
    for index, elem in enumerate(string.split('.')):
        new_table[index // size][index % size] = int(elem)
    return new_table


@jit(nopython=True, fastmath=True)
def associative_test(table, n: int) -> bool:
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if table[table[x][y]][z] != table[x][table[y][z]]:
                    return 0
    return 1


# @jit(nopython=True)  не хочет функцию int понимать
def count(k):
    c = 0
    for i in range(k**(k*k)):
        table = array([[0 for _ in range(k)] for _ in range(k)])
        for index, elem in enumerate(to_system(i, k).split('.')):
            table[index // k][index % k] = int(elem)
        c += 1 if associative_test(table, k) else 0
    return c

def main():
    k = int(input())
    print(count(k))


if __name__ == "__main__":
    main()
