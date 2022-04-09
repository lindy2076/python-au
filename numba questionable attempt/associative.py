def to_system(num: int, base: int) -> str:  # генерация строки таблицы
    if num == 0:
        res = '0'
    else:
        res = str(num % base)
        num //= base
    while num > 0:
        res = str(num % base) + '.' + res
        num //= base
    while len(res.split('.')) < base**2:
        res = str(0) + '.' + res
    return res


def generate_table(num: int, size: int) -> list[list]:  # генерация самой таблицы из строки
    string = to_system(num, size)
    new_table = [[0 for _ in range(size)] for _ in range(size)]
    for index, elem in enumerate(string.split('.')):
        new_table[index // size][index % size] = int(elem)
    return new_table


def associative_test(table: list[list], n: int) -> bool:
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if table[table[x][y]][z] != table[x][table[y][z]]:
                    return 0
    return 1


def count(k):
    c = 0
    for i in range(k**(k*k)):
        c += 1 if associative_test(generate_table(i, k), k) else 0
        # if (i % 100000 == 0):
        #     print(".")
    return c


def main():
    k = int(input())
    print(count(k))


if __name__ == "__main__":
    main()
