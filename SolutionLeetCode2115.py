from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)

        supplies_set = set()
        recipe_book = {}

        for supply in supplies:
            supplies_set.add(supply)

        for i in range(n):
            recipe = recipes[i]
            ingredients_for_recipe = ingredients[i]
            recipe_book[recipe] = ingredients_for_recipe

        prepared_recipes = set()

        while True:
            initial_nb_prepared_recipes = len(prepared_recipes)

            for recipe in recipe_book:
                was_prepared = True
                # Check if we have all the necessary ingredients
                for ingredient in recipe_book[recipe]:
                    if ingredient not in supplies_set:
                        was_prepared = False
                        break
                # Update prepared recipes
                if was_prepared:
                    prepared_recipes.add(recipe)
            # Add prepared recipes to the list of supplies
            # and remove from the recipe book (we have already prepared them)
            for recipe in prepared_recipes:
                supplies_set.add(recipe)
                if recipe in recipe_book:
                    del recipe_book[recipe]
            # Exit the while loop if we haven’t prepared a new recipe
            if len(prepared_recipes) == initial_nb_prepared_recipes:
                break

        return list(prepared_recipes)
