from python99.lists.p127 import group
import functools
import operator


def test_group():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    nums = [3, 5, 2]
    actual = group(l, nums)
    for resolution in actual:
        # each possibility has correct number of groups
        assert len(resolution) == len(nums)
        for index, value in enumerate(nums):
            # each group has correct number of elements
            assert len(resolution[index]) == value
        # all groups are disjoint
        assert len(set(functools.reduce(
            operator.concat, resolution, []))) == len(l)
        # all elements are in origin list
        assert functools.reduce(operator.and_, [e in l for e in functools.reduce(
            operator.concat, resolution, [])], True) == True
    total = 1
    m = len(l)
    for num in nums:
        total = total * functools.reduce(operator.mul, range(m-num+1, m+1), 1)/functools.reduce(
            operator.mul, range(1, num+1), 1)
        m = m - num
    # it includes all resolutions
    assert len(actual) == total
