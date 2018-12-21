from python99.lists.p127 import group
import functools
import operator

def test_group():
    l = [1,2,3,4,5,6,7,8,9,0]
    nums = [3,5,2]
    actual = group(l,nums)
    for e in actual:
        # each possibility has correct number of groups
        assert len(e) == len(nums)
        for index, value in enumerate(nums):
            # each group has correct number of elements
            assert len(e[index]) == value
        # all groups are disjoint
        assert len(set(functools.reduce(operator.concat,e,[]))) == len(l)
