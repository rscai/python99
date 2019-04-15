from functools import reduce
from operator import concat

def puzzle(nums):
    leftAndRightNums = []
    for splitPoint in range(1, len(nums)):
        leftAndRightNums.append((nums[:splitPoint], nums[splitPoint:]))
    trees = reduce(concat,[[['==',left, right] 
                for left in buildBTrees(num[0])
                for right in buildBTrees(num[1])] 
                for num in leftAndRightNums],
                [])
    exprs = [btreeToExpr(tree)[1] for tree in trees]
    uniqueExprs =[]
    for expr in exprs:
        if expr not in uniqueExprs:
            uniqueExprs.append(expr)
    return [expr for expr in uniqueExprs if eval(expr)]


def buildBTrees(l):
    if len(l) == 0:
        return [None]
    if len(l) == 1:
        return l
    ops = ['+', '-', '*', '/']
    leftAndRightNums = []
    for splitPoint in range(1, len(l)):
        leftAndRightNums.append((l[:splitPoint], l[splitPoint:]))
    return reduce(concat, [[[op, left, right]
            for op in ops
            for left in buildBTrees(nums[0])
            for right in buildBTrees(nums[1])]
            for nums in leftAndRightNums],
            [])


def btreeToExpr(tree):
    if type(tree) is not list:
        return str(tree), str(tree)
    if tree[1] is None and tree[2] is None:
        return str(tree[0]), str(tree[0])
    leftOp, leftExpr = btreeToExpr(tree[1])
    rightOp, rightExpr = btreeToExpr(tree[2])
    op = tree[0]
    if greaterPrecedence(op, leftOp):
        leftExpr = '('+leftExpr+')'
    if greaterPrecedence(op, rightOp):
        rightExpr = '('+rightExpr + ')'
    return op, leftExpr + op+rightExpr


def greaterPrecedence(left, right):
    precedenceDict = {
        '==':0,
        '-': 1,
        '+': 1,
        '*': 2,
        '/': 2
    }
    # operand precedence is greater than operator
    if right not in precedenceDict:
        return False
    return precedenceDict[left] > precedenceDict[right]

