from python99.lists.p104 import find_element_number

def test_find_element_number():
    assert find_element_number([1,3,4,5,'Apple','Orange']) == 6
    assert find_element_number(None) == 0