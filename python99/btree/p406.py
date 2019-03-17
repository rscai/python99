def hbal_tree(n):
    E = 'E'
    if n == 0:
        return [None]
    if n == 1:
        return [[E, None, None]]
    n_one_subtree = hbal_tree(n-1)
    n_two_subtree = hbal_tree(n-2)
    tree_a = [[E, left, right]
              for left in n_one_subtree for right in n_one_subtree]
    tree_b = [[E, left, right]
              for left in n_one_subtree for right in n_two_subtree]
    tree_c = [[E, left, right]
              for left in n_two_subtree for right in n_one_subtree]
    return tree_a + tree_b + tree_c
