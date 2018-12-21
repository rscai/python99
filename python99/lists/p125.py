# Generate a random permutation of the elements of a list.
# Hint: Use the solution of problem 1.23

import random


def rnd_permu(l):
    return random.sample(l, len(l))
