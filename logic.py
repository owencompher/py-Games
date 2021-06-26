def xor(a, b):  return (a or b) and not (a and b)
def xnor(a, b): return not (a or b) or (a and b)
def andall(*args):
    for i in args:
        if not i:
            return False
    return True