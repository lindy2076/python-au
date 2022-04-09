def generate_table(num: int, size: int) -> list[list]:  # генерация самой таблицы из строки
    new_table = [[0] * size for _ in range(size)]
    c, r = size - 1, size - 1
    while num:
        new_table[r][c] = num % size
        if not c:
            c = size
            r -= 1
        c -= 1
        num //= size
    # print(new_table)
    return new_table


def associative_test(table: list[list], n: int) -> bool:
    for x in range(n):
        for y in range(n):
            for z in range(n):
                if table[table[x][y]][z] != table[x][table[y][z]]:
                    return 0
    return 1


def associative_test_optimized(table: list[list], n: int) -> bool:
    
    return 1


def count(k):
    c = 0
    for i in range(k**(k*k)):
        c += associative_test(generate_table(i, k), k)
        # if (i % 100000 == 0 and i != 0):
        #     break
    return c


def main():
    k = int(input())
    print(count(k))


if __name__ == "__main__":
    main()
