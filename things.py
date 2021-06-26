def dict_from_lists(keys, values):
    """Convert two lists into a dictionary, first list being the keys
    and the second being the values
    """
    pairs = [(variables[i].name, var_values[i]) for i in range(len(variables))]
    return dict(pairs)

class Tree:
    def __init__(self):
        self.branches = []

def char_occurrences(string: str, char: str):
    """Return a list of the indexes of every occurrence of a character
     in a string
     """
    occurrences = []
    for i in range(len(string)):
        if string[i] == char:
            occurrences.append(i)
    return occurrences


