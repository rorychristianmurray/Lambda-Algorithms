#!/usr/bin/python

import argparse

lister = [3, 9, 7, 1, 16, 12, 4]


def find_max_profit(prices):

    # note first value of array (base case) as the current_min
    # note first index of array (base case) as the current_mindex
    # iterate over the prices list

    # base case for min
    min = prices[0]
    mindex = 0

    for i in range(len(prices) - 1):
        print(f"min val before : {min}")
        print(f"mindex before : {mindex}")
        if prices[i] < min:
            min = prices[i]
            mindex = i
            print(f"min val after : {min}")
            print(f"mindex after : {min}")

    # iterate over the array from range(current_mindex, len(arr) - 1)
    # Compute profit and note it as current_max_profit
    # If encounter larger profit, note it as current_max_profit
        # for i in range(mindex, len(arr) - 1):

    print(f"global min : {min}")
    print(f"global mindex : {mindex}")

    # Continue original loop
    # Do we encounter a value that is smaller than the `current_min`?
    # If yes, then overwrite the current_min and run the profit loop again from range(current_min, len(arr) - 1)

    return min


# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))


test1 = find_max_profit(lister)
