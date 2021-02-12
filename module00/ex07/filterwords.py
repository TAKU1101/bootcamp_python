import sys
import re

if __name__ == "__main__":
    argc = len(sys.argv)
    try:
        if argc != 3 or sys.argv[1].isdigit():
            raise
        word_list = re.split("[ !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~\n\t\r\v\f]", sys.argv[1])
        word_list = [word for word in word_list if len(word) > int(sys.argv[2])]
        print(word_list)
    except:
        print("ERROR")