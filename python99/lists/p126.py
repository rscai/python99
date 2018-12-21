# Generate the combinations of K distinct objects chosen from the N elements of a list
# In how many ways can a committee of 3 be chosen from a group of 12 people?
# We all know that there are C(12,3) = 200 possibilities (C(n,k) denotes the well-known binomial coefficients).
# For pure mathematicians, this result may be great. But we want to realy generate all the possiblities (via backtracking)


def combination(l, k):
    if k == 1:
        return [[e] for e in l]
    elements = [(i, e) for i, e in enumerate(l)]
    return [[e[1]]+remain_combination for e in elements for remain_combination in combination(l[e[0]+1:], k-1)]
