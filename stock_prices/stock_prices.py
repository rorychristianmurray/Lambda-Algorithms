#!/usr/bin/python

import argparse

lister = [3, 9, 7, 1, 16, 12, 4]


def find_max_profit(prices):

    # note first value of array (base case) as the current_min
    # note first index of array (base case) as the current_mindex
    # iterate over the prices list

    # base case for min and max
    min = prices[0]
    mindex = 0
    max = prices[1]
    max_profit = max - min

    for i in range(mindex, len(prices) - 1):
        # Continue original loop
        # Do we encounter a value that is smaller than the `current_min`?
        # If yes, then overwrite the current_min and run the profit loop again from range(current_min, len(arr) - 1)
        if prices[i] < min:
            min = prices[i]
            mindex = i
            print(f"min val after : {min}\n mindex after : {min}\n")

    # iterate over the array from range(current_mindex, len(arr) - 1)
    # Compute profit and note it as current_max_profit
    # If encounter larger profit, note it as current_max_profit

        elif prices[i] - min > max_profit:
            print(f"prices[i] {prices[i]}\n min {min}\n")
            max_profit = prices[i] - min
            print(f"max profit after : {max_profit}\n")

    print(f"global min : {min}\n")
    print(f"global mindex : {mindex}\n")
    print(f"global max_profit : {max_profit}\n")

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))


test1 = find_max_profit(lister)
