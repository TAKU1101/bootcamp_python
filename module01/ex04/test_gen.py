from generator import generator

if __name__ == '__main__':
    print("============ shuffle option ============")
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, option="shuffle"):
        print(word)

    print("============ ordered option ============")
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, option="ordered"):
        print(word)

    print("============ unique option ============")
    text = "Lorem Ipsum Lorem Ipsum"
    for word in generator(text, option="unique"):
        print(word)

    print("============ no option ============")
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text):
        print(word)

    for word in generator(1.0):
        print(word)
