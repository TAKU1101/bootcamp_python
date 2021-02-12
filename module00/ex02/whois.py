import sys

def odd_or_even(d: str) -> str:
    n = int(d)
    if n == 0:
        return "Zero"
    elif n % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == '__main__':
    argc = len(sys.argv)
    try:
        if argc == 2:
            mes = odd_or_even(sys.argv[1])
            print("I'm {}.".format(mes))
        elif argc > 2:
            raise
    except:
        print("ERROR")
