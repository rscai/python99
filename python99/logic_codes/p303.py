# Truth tables for logic expressions
# Generalize problem 3.02 in such a way that the
# logical expression may contain any number of logical 
# variables. Define table/2 in a way that table(List, Expr)
# prints the truth table for the expression Expr, which 
# contains the logical variables enymerated in list.
from python99.logic_codes.p302 import postOrderTraversal,buildTreeFrom,tokenize,evaluate

def table(variables, expr):
    postExpr = postOrderTraversal(buildTreeFrom(tokenize(expr)))
    inputTable = constructInputs([(k,v) for k,v in variables.items()])
    result = [extractValue(input) +[evaluate(resolveVariable(postExpr,input))] for input in inputTable]
    return [tuple(e) for e in result]

def extractValue(kvs):
    return [e[1] for e in kvs]

def constructInputs(variables):
    if len(variables)==1:
        e = variables[0]
        return [[(e[0],v)] for v in e[1]]
    e = variables[0]
    kv = [(e[0],v) for v in e[1]]
    print(kv)
    return [[first] + remain for first in kv for remain in constructInputs(variables[1:])]

def resolveVariable(expr, input):
    resolved = []
    kv = {}
    for e in input:
        kv[e[0]]=e[1]
    for e in expr:
        if e in kv:
            resolved.append(kv[e])
        else:
            resolved.append(e)
    return resolved
