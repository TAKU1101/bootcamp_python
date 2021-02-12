from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name: str):
        self.name = name
        self.creation_date = datetime.now()
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": [],
        }
        self.last_date = self.creation_date

    def get_recipe_by_name(self, name: str):
        for food_type in ["starter", "lunch", "dessert"]:
            for recipe in self.recipes_list[food_type]:
                if (recipe.name == name):
                    print(recipe)

    def get_recipe_by_type(self, recipe_type: str):
        for recipe in self.recipes_list[recipe_type]:
            print(recipe)

    def add_recipe(self, recipe: Recipe):
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_date = datetime.now()

if __name__ == '__main__':
    book = Book("recipe book")

    recipe = Recipe("food", 5, 5, ["ham", "egg", "spam"], "food", "lunch")
    book.add_recipe(recipe)
    book.get_recipe_by_name("food")
    book.get_recipe_by_type("lunch")
