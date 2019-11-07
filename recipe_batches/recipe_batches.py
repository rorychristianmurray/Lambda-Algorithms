#!/usr/bin/python

import math

r1 = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
r2 = {'milk': 100, 'butter': 50, 'cheese': 10}
r3 = {'milk': 2, 'sugar': 40, 'butter': 20}

l1 = {'milk': 1288, 'flour': 9, 'sugar': 95}
l2 = dict([('milk', 198), ('butter', 50), ('cheese', 10), ])
l3 = {'milk': 5, 'sugar': 120, 'butter': 500}


def recipe_batches(recipe, ingredients):
    # print recipe and larder
    print(f"recipe : {recipe}\n larder : {ingredients}\n")

    # establsh base case
    batches = 0
    recipe_keys = []
    larder_keys = []
    recipe_items = []
    larder_items = []
    checker = []

    # compare keys in recipe to keys in larder
    # if ingredient for recipe is missing, kill process
    # create new list from each of just keys
    for k, v in recipe.items():
        recipe_keys.append(k)

    for k, v in ingredients.items():
        larder_keys.append(k)

    for i in recipe_keys:
        if i not in larder_keys:
            print(
                f"we do not have {i} in the larder and cannot make this recipe")
            return batches

    # create new list of values in recipe
    # create new list of values in larder
    # compare values in recipe to values in larder
    # divide value in larder using integer division
    # and store it in a new list
    # once thats done, select minimum val
    # from list to get potential whole batches
    for k, v in recipe.items():
        recipe_items.append(v)

    for k, v in ingredients.items():
        larder_items.append(v)

    for i in range(len(larder_items)):
        checker.append(larder_items[i]//recipe_items[i])
        print(
            f"larder_items[i] : {larder_items[i]}\nrecipe_items[i] : {recipe_items[i]}")

    batches = min(checker)

    print(f"recipe_items : {recipe_items}")
    print(f"larder_items : {larder_items}")
    print(f"checker : {checker}")

    # return batches
    return f"you have made {batches} whole batches!"


# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


# test1 = recipe_batches(r1, l1)
# print(test1)

#


test3 = recipe_batches(r3, l3)
print(test3)

# test2 = recipe_batches(r2, l2)
