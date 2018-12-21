# Lotto: Draw N different random numbers from the set 1..M
# The selected numbers shall be put into a result list

import random


def lotto(n, m):
    return random.sample(range(1, m+1), n)
