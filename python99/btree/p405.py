from python99.btree.p402 import cbal_tree
from python99.btree.p403 import symmetric

def sym_cbal_trees(n):
    trees = cbal_tree(n)
    return [tree for tree in trees if symmetric(tree) is True]