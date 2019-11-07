#!/usr/bin/python

import math

r1 = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
r2 = {'milk': 1288, 'flour': 9, 'sugar': 95}

l1 = {'milk': 2, 'sugar': 40, 'butter': 20}
l2 = dict([('milk', 5), ('sugar', 120), ('butter', 500), ])


def recipe_batches(recipe, ingredients):
    # print recipe and larder
    print(f"recipe : {recipe}\n larder : {ingredients}\n")

    # get k:v using items() method
    for k, v in recipe.items():
        print(f"k : {k}\nv : {v}\n")

    # retrieve position index and corresponding value
    # using the enumerate() function
    for i, v in enumerate(recipe):
        print(f"i : {i}\nv : {v}\n")

    # loop over both recipe and larder sequence
    # by pairing them with a zip() function
    for ingredient, amount in zip(r1, l1):
        print(
            f"The recipe calls for {ingredient}, we have {amount} in the larder")

    # establsh base case
    batches = 0

    return batches


# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))


test1 = recipe_batches(r1, l1)

# test2 = recipe_batches(r2, l2)
