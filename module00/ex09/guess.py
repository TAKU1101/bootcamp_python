import random

def promt_input(mes: str) -> str:
    s = ""
    while s == "":
        print(mes, end=" ")
        s = input()
    return s

def print_clearmes(n: int, count: int):
    if n == 42:
        print("The answer to the ultimate question of life, the universe and everything is 42.")
    if count == 1:
        print("Congratulations! You got it on your first try!")
    else:
        print("You won in {} attempts!".format(count))


if __name__ == "__main__":
    n = random.randint(1, 99)
    count = 0
    ans = -1

    print("""This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!""", end="\n\n")
    n = 42
    while n != ans:
        try:
            count += 1
            print("What's your guess between 1 and 99?")
            ans = promt_input(">>")
            if ans == "exit":
                print("Goodbye!")
                break
            ans = int(ans)
            if n == ans:
                print_clearmes(n, count)
            else:
                print("Too {}!".format("low" if ans < n else "high"))
        except ValueError:
            print("That's not a number.")
