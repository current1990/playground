def get_input():
    num1 = input("Please input number 1:")
    num2 = input("Please input number 2:")
    return int(num1), int(num2)


def karatsuba(n1, n2):
    if n1 < 10 or n2 < 10:
        return n1 * n2

    n1str = str(n1)
    n2str = str(n2)
    pos = max(len(n1str), len(n2str)) / 2

    x1 = 0 if n1str[:-pos] == '' else int(n1str[:-pos])
    x0 = 0 if n1str[-pos:] == '' else int(n1str[-pos:])
    y1 = 0 if n2str[:-pos] == '' else int(n2str[:-pos])
    y0 = 0 if n2str[-pos:] == '' else int(n2str[-pos:])

    z0 = karatsuba(x0, y0)
    z1 = karatsuba((x1 + x0), (y1 + y0))
    z2 = karatsuba(x1, y1)

    return z2 * 10 ** (2 * pos) + (z1 - z2 - z0) * 10 ** pos + z0


if __name__ == "__main__":
    number1, number2 = get_input()
    print karatsuba(number1, number2)
