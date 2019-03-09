# Huffman code

def huffman(fs):
    sortedFs = sorted(fs,key=lambda f: f[1])
    tree = constructTree(sortedFs)
    return sorted(traversal(tree[0]),key=lambda x:x[0])

def constructTree(sortedList):
    if len(sortedList) ==1:
        return sortedList
    result =[]
    for i in range(0, len(sortedList),2):
        e = sortedList[i]
        if i+1 >= len(sortedList):
            result.append(e)
        else:
            result.append([e,sortedList[i+1]])
    return constructTree(result)


def traversal(tree):
    if type(tree) is tuple:
        # leaf
        return [(tree[0],'')]
    leftHs = []
    rightHs = []
    if len(tree) > 0:
        # has left child
        leftHs = [(lambda e: (e[0],'0'+e[1]))(e) for e in traversal(tree[0])]
    if len(tree) > 1:
        # has right child
        rightHs = [(lambda e: (e[0],'1'+e[1]))(e) for e in traversal(tree[1])]
    return leftHs + rightHs
