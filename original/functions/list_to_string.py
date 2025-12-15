from functools import reduce

def list_to_string(list_string, delim):
    string = reduce(lambda x, y: str(x) + delim + str(y), list_string)
    return string
