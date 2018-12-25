## Find out whether a list is a palindrome.
## A palindrome can be read forward or backward


def is_palindrome(list):
    if list is None:
        return False
    if len(list) == 0:
        return True
    if len(list) == 1:
        return True
    start_index = 0
    end_index = len(list)-1
    ## slicing range is (inclusive, exclusive)
    return list[start_index] == list[end_index] and is_palindrome(list[start_index+1:end_index])
