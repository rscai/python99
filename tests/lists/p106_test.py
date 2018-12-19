from python99.lists.p106 import is_palindrome

def test_is_palindrome():
    assert is_palindrome([]) == True
    assert is_palindrome([1]) == True
    assert is_palindrome([1,2,3,4,3,2,1]) == True
    assert is_palindrome([1,2,3,4,4,3,2,1]) == True
    assert is_palindrome([1,2,3,2,2]) ==  False