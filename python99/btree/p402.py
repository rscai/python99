import itertools

def cbal_tree(n):
    if n == 0:
        return [None]
    element = 'E'
    num_of_right = (n-1)//2
    num_of_left = (n - 1) - num_of_right
    a = [[element, left, right] for left in cbal_tree(num_of_left) for right in cbal_tree(num_of_right)]
    b = [[element, left, right] for left in cbal_tree(num_of_right) for right in cbal_tree(num_of_left)]
    result = a + b
    return [ii for n,ii in enumerate(result) if ii not in result[:n]]
