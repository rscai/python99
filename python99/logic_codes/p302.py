# Truth tables for logical expressions (2)
# Contibue problem 3.01 by defining and/2, or/2, etc as being  operators.
# this allows to write the logical expression in the more natural way,
# as in the example: AS and (A or not B).
# define operator precedence as usual; i.e. as in Java.


def table(la, lb, expr):
    postExpr = postOrderTraversal(buildTreeFrom(tokenize(expr)))
    return [(a,b,evaluate(resolveVariable(postExpr,{'A':a,'B':b}))) for a in la for b in lb]

def resolveVariable(expr, keyValues):
    resolved = []
    for e in expr:
        if e in keyValues:
            resolved.append(keyValues[e])
        else:
            resolved.append(e)
    return resolved


def tokenize(exprInStr):
    SA = 1
    SB = 2
    paren = ['(', ')']
    space = [' ']
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    state = SA
    tokens = []
    wordCache = []
    for e in exprInStr + ' ':
        if state == SA and e in space:
            # Nop
            pass
        elif state == SA and e in alphabet:
            wordCache.append(e)
            state = SB
        elif state == SA and e in paren:
            tokens.append(e)
            # stay at SA
        elif state == SB and e in alphabet:
            wordCache.append(e)
            # stay at SB
        elif state == SB and e in space:
            tokens.append(''.join(wordCache))
            wordCache = []
            state = SA
        elif state == SB and e in paren:
            tokens.append(''.join(wordCache))
            wordCache = []
            tokens.append(e)
            state = SA
        else:
            pass
    return [e for e in tokens if len(e) != 0]

def postOrderTraversal(tree):
    l = []
    if tree.firstChild() is not None:
        l = l + postOrderTraversal(tree.firstChild())
    if tree.secondChild() is not None:
        l = l + postOrderTraversal(tree.secondChild())
    l.append(tree.value[0])
    return l

def buildTreeFrom(listFormInExpr):
    tree = None
    lastNode = None
    for e in listFormInExpr:
        node = buildExprNode(e)
        tree, lastNode = insertIntoTreeFrom(tree, node, lastNode)
    return tree


def insertIntoTreeFrom(tree, node, lastTouchedNode):
    if tree is None:
        return (node, node)
    if node.value[0] == ')':
        return insertRightBracket(tree, node, lastTouchedNode)
    return insertOthers(tree, node, lastTouchedNode)


def insertRightBracket(tree, node, lastTouchedNode):
    currentNode = lastTouchedNode
    while currentNode is not None and currentNode.value[0] != '(':
        currentNode = currentNode.parent
    parent = currentNode.parent
    parent.removeChild(currentNode)
    parent.addChild(currentNode.firstChild())
    return (tree, currentNode.firstChild())


def insertOthers(tree, node, lastTouchNode):
    if node.value[1] > lastTouchNode.value[1]:
        lastTouchNode.addChild(node)
        return (tree, node)
    currentNode = lastTouchNode
    while currentNode.parent is not None and currentNode.value[0] != '(' and node.value[1] <= currentNode.value[1]:
        currentNode = currentNode.parent
    if currentNode.parent is None:
        node.addChild(currentNode)
        return (node, node)
    node._children = currentNode._children
    currentNode._children = []
    currentNode.addChild(node)
    return (tree, node)


def buildExprNode(symbol):
    bracketSymbols = ['(', ')']
    highPrecedenceOperators = ['not']
    mediumPrecedenceOperators = ['and', 'nand', 'nor', 'xor', 'impl']
    lowPrecedenceOperators = ['or', 'equ']

    LOW_PRECEDENCE = 10
    MEDIUM_PRECEDENCE = LOW_PRECEDENCE+1
    HIGH_PRECEDENCE = MEDIUM_PRECEDENCE+1
    BRACKET_PRECEDENCE = HIGH_PRECEDENCE+1
    OPERAND_PRECEDENCE = BRACKET_PRECEDENCE+1

    if symbol in bracketSymbols:
        return Node((symbol, BRACKET_PRECEDENCE))
    if symbol in highPrecedenceOperators:
        return Node((symbol, HIGH_PRECEDENCE))
    if symbol in mediumPrecedenceOperators:
        return Node((symbol, MEDIUM_PRECEDENCE))
    if symbol in lowPrecedenceOperators:
        return Node((symbol, LOW_PRECEDENCE))
    return Node((symbol, OPERAND_PRECEDENCE))


class Node:
    def __init__(self, value):
        self.value = value
        self._children = []
        self.parent = None

    def addChild(self, node):
        self._children.append(node)
        node.parent = self

    def removeChild(self, node):
        self._children = [e for e in self._children if e.value != node.value]

    def firstChild(self):
        if len(self._children) > 0:
            return self._children[0]
        else:
            return None
    def secondChild(self):
        if len(self._children) >=2:
            return self._children[1]
        else:
            return None

def evaluate(exprInList):
    stack = []
    operatorBuilder = OperatorBuilder()
    for e in exprInList:
        if type(e) == bool:
            stack.append(e)
        else:
            op = operatorBuilder.buildFor(e)
            if op.isUnary():
                a = stack.pop()
                stack.append(op.apply(a))
            elif op.isBinary():
                a = stack.pop()
                b = stack.pop()
                stack.append(op.apply(a, b))
            else:
                raise "Unsupported operator " + e
    return stack.pop()


class Operator:
    def __init__(self, symbol):
        self.symbol = symbol

    def isUnary(self):
        return False

    def isBinary(self):
        return False

    def apply(self, a, b=None):
        raise NotImplementedError


class Not(Operator):
    def __init__(self):
        super().__init__('not')

    def isUnary(self):
        return True

    def apply(self, a):
        return not a


class And(Operator):
    def __init__(self):
        super().__init__('and')

    def isBinary(self):
        return True

    def apply(self, a, b):
        return a and b


class Or(Operator):
    def __init__(self):
        super().__init__('or')

    def isBinary(self):
        return True

    def apply(self, a, b):
        return a or b


class Nand(Operator):
    def __init__(self):
        super().__init__('nand')

    def isBinary(self):
        return True

    def apply(self, a, b):
        return not (a and b)


class Nor(Operator):
    def __init__(self):
        super().__init__('nor')

    def isBinary(self):
        return True

    def apply(self, a, b):
        return not (a or b)


class Xor(Operator):
    def __init__(self):
        super().__init__('xor')

    def isBinary(self):
        return True

    def apply(self, a, b):
        return a != b


class Impl(Operator):
    def __init__(self):
        super().__init__('impl')

    def isBinary(self):
        return True

    def apply(self, a, b):
        return (not a) or b


class Equ(Operator):
    def __init__(self):
        super().__init__('equ')

    def isBinary(self):
        return True

    def apply(self, a, b):
        return a == b


class Nop(Operator):
    def __init__(self):
        super().__init__('op')


class OperatorBuilder:
    def __init__(self):
        self._operatorDefinition = {
            Not().symbol: Not(),
            And().symbol: And(),
            Or().symbol: Or(),
            Nand().symbol: Nand(),
            Nor().symbol: Nor(),
            Xor().symbol: Xor(),
            Impl().symbol: Impl(),
            Equ().symbol: Equ()
        }

    def buildFor(self, symbol):
        if symbol in self._operatorDefinition:
            return self._operatorDefinition[symbol]
        else:
            return Nop()
