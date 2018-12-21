# Decode a run-length encoded list.
# Given a run-length code list generated as specified in problem 1.11.
# Construct its uncompressed version

from python99.lists.p107 import flatten

def decode(l):
    if l is None:
        return []
    if len(l) == 0:
        return []
    return flatten([ decode_term(term) for term in l])

def decode_term(term):
    if isinstance(term, list):
        return [ term[1] for e in range(0,term[0])]
    else:
        return term