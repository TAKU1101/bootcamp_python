import sys
import re

morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": ".----",
    "1": "..---",
    "2": "...--",
    "3": "....-",
    "4": ".....",
    "5": "-....",
    "6": "--...",
    "7": "---..",
    "8": "----.",
    "9": "-----",
}

if __name__ == "__main__":
    try:
        for arg in sys.argv[1:]:
            if len(re.findall("[^a-zA-Z0-9 ]", arg)) > 0:
                raise
        morse_mes = []
        for arg in sys.argv[1:]:
            mes = re.split(" ", arg.upper().strip())
            for word in mes:
                morse_word = []
                for char in word:
                    morse_word.append(morse[char])
                morse_mes.append(" ".join(morse_word))
        print(" / ".join(morse_mes))
    except:
        print("ERROR")
