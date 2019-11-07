#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):
    # print(f"There are {n} cookies in the cookie jar!")

    # base case
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        print(f"n : {n}\nn + eating_cookies(n - 1) {n + eating_cookies(n - 1)}\n")
        return n + eating_cookies(n - 2)


# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')


test1 = eating_cookies(3)
print(test1)
