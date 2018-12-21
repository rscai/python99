# Group the elements of a set into disjoint subsets.
# a) In how many ways can a group of 9 people work in 3 disjoint subgroups of 2, 3 and 4 persons?
# Write a predicate that generates all the possibilities via backtracking.
from python99.lists.p126 import combination

# group l into len(nums) subsets, nums imply number of groups respectively
def group(l,nums):
    if len(nums) == 1:
        return [combination(l,nums[0])]
    first_group = combination(l,nums[0])
    return [[first_group_element] + remain_group_e 
            for first_group_element in first_group 
            for remain_group_e in group(list(set(l)-set(first_group_element)), nums[1:])
        ]
