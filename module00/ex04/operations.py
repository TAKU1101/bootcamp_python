import sys

def calculator(x: int, y: int):
    print("Sum:        {}".format(x + y))
    print("Differnce:  {}".format(x - y))
    print("Product:    {}".format(x * y))
    try:
        print("Quotient:   ", end="")
        n = x / y
        print(n)
    except ZeroDivisionError:
        print("ERROR (div by zero)")
    try:
        print("Remainder:  ", end="")
        n = x % y
        print(n)
    except ZeroDivisionError:
        print("ERROR (modulo by zero)")

if __name__ == '__main__':
    argc = len(sys.argv)
    try:
        if argc > 3:
            raise
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        calculator(x, y)
    except:
        print("""InputError: only numbers

Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3""")