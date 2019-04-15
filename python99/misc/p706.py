INITIALIZED = 'INITIALIZED'
LETTER = 'LETTER'
HYPHEN = 'HYPHEN'
DIGIT = 'DIGIT'
INVALID = 'INVALID'


def identifier(expr):
    syntaxChecker = DFA(syntaxDfaTransition, INITIALIZED,
                        set([LETTER, DIGIT]))
    for s in expr:
        syntaxChecker.input(s)
    return syntaxChecker.isAcceptable()


class DFA:
    def __init__(self, transition, startState, acceptStates):
        self.transition = transition
        self.state = startState
        self.acceptStates = acceptStates

    def input(self, s):
        self.state = self.transition(self.state, s)

    def isAcceptable(self):
        return self.state in self.acceptStates


def syntaxDfaTransition(state, event):
    if state == INITIALIZED and isLetter(event):
        return LETTER
    if state == INITIALIZED and isHyphen(event):
        return INVALID
    if state == INITIALIZED and isDigit(event):
        return INVALID
    if state == INITIALIZED and isOther(event):
        return INVALID
    if state == LETTER and isLetter(event):
        return LETTER
    if state == LETTER and isHyphen(event):
        return HYPHEN
    if state == LETTER and isDigit(event):
        return DIGIT
    if state == LETTER and isOther(event):
        return INVALID
    if state == HYPHEN and isLetter(event):
        return LETTER
    if state == HYPHEN and isHyphen(event):
        return INVALID
    if state == HYPHEN and isDigit(event):
        return DIGIT
    if state == HYPHEN and isOther(event):
        return INVALID
    if state == DIGIT and isLetter(event):
        return LETTER
    if state == DIGIT and isHyphen(event):
        return HYPHEN
    if state == DIGIT and isDigit(event):
        return DIGIT
    if state == DIGIT and isOther(event):
        return INVALID
    if state == INVALID and isLetter(event):
        return INVALID
    if state == INVALID and isHyphen(event):
        return INVALID
    if state == INVALID and isDigit(event):
        return INVALID
    if state == INVALID and isOther(event):
        return INVALID


def isLetter(event):
    return event.isalpha()


def isHyphen(event):
    return event == '-'


def isDigit(event):
    return event.isdigit()


def isOther(event):
    return not (isLetter(event) or isHyphen(event) or isDigit(event))
