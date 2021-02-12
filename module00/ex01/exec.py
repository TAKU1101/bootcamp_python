import sys

if __name__ == '__main__':
    rev = " ".join(sys.argv[1:])[::-1].swapcase()
    print(rev)