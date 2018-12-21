# Extract a given number of randomly selected elements from a list.
# The selected items shall be put into a result list

import random


def rnd_select(l, n):
    return random.sample(l, n)
