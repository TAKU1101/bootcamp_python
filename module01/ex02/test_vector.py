from vector import Vector

if __name__ == '__main__':
    v1 = Vector([1, 2, 3, 4])
    v2 = Vector([5, 6, 7, 8])

    print(v1 + 4)
    print(4 + v1)
    print(v1 + v2)

    print(v1 - 4)
    print(4 - v1)
    print(v1 - v2)

    print(v1 * 4)
    print(4 * v1)
    print(v1 * v2)

    print(v1 / 4)
    print(4 / v1)
    print(v1 / v2)

    print(v1)
    print(v2)