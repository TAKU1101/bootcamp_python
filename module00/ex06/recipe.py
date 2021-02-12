cookbook = {
    "sandwith" : {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal" : "lunch",
        "prep_time" : 10,
    },
    "cake" : {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal" : "dessert",
        "prep_time" : 60,
    },
    "salad" : {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal" : "lunch",
        "prep_time" : 15,
    },
}

def adinput(prompt: str) -> str:
    s = ""
    while s == "":
        print(prompt, "", end="")
        s = input()
    return (s)


def print_recipes(name: str):
    try:
        recipe = cookbook[name]
        print("Ingredients list: {}".format(recipe["ingredients"]))
        print("To be eaten for {}.".format(recipe["meal"]))
        print("Takes {} minutes of cooking.".format(recipe["prep_time"]))
    except KeyError:
        print("There is no recipe by that name.")

def del_one_recipes(name: str):
    try:
        del cookbook[name]
    except KeyError:
        print("There is no recipe by that name.")

def add_recipes(name: str, ingredients: list, meal: str, prep_time: int):
    recipe = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time,
    }
    cookbook[name] = recipe

def input_recipes():
    ingredient = ""
    ingredients = []

    print("Enter the name of the dish.")
    # print("> ", end="")
    # name = input()
    name = adinput(">")

    print("""Please enter the ingredients you want to use,
and enter the EOF at the end.""")
    while True:
        print("> ", end="")
        ingredient = input()
        if ingredient == "EOF":
            break
        ingredients.append(ingredient)
    
    print("Please enter the type of meal. Lunch, dessert, etc.")
    # print("> ", end="")
    # meal = input()
    meal = adinput(">")

    print("Enter the time it will take to prepare")
    while True:
        # print("> ", end="")
        # prep_time = input()
        prep_time = adinput(">")
        if prep_time.isdigit():
            break
    prep_time = int(prep_time)

    add_recipes(name, ingredients, meal, prep_time)

def print_all_recipes():
    for key in cookbook.keys():
        print("======================= {:^20} ==========================".format(key), end="\n\n")
        print_recipes(key)
        print("")

def print_alternatives():
    print("""1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit""")

def prompt():
    q = 0
    print_alternatives()
    while q != 5:
        try:
            # print(">> ", end="")
            # q = input()
            q = adinput(">>")
            print("", end="\n\n")
            q = int(q)
            if q == 1:
                input_recipes()
            elif q == 2:
                print("Entering a name will delete that recipe:")
                # print("> ", end="")
                # name = input()
                name = adinput(">")
                del_one_recipes(name)
            elif q == 3:
                print("Please enter the recipe's name to get its details:")
                # print("> ", end="")
                # name = input()
                name = adinput(">")
                print_recipes(name)
            elif q == 4:
                print_all_recipes()
            elif q == 5:
                print("Cookbook closed.")
            else:
                raise
        except:
            print("""This option does not exist, please type the corresponding number.
To exit, enter 5.""", end="\n")
        print("\n")

if __name__ == '__main__':
    prompt()