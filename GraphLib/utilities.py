from copy import copy
from typing import List


def functional_copy(destination: tuple, item, key: int) -> tuple:

    if key == 0:
        return (item,) + destination[1:]

    if key + 1 == len(destination):
        return destination[:len(destination) - 1] + (item,)

    return destination[:key - 1] + (item,) + destination[key + 1:]


def no_duplicate(li_):
    nl = []
    for a in li_:
        if a not in nl:
            nl.append(a)
    return nl


def weird_matching(list_end: list, list_begin: list) -> List[list]:

    base = len(list_end)
    n_digits = len(list_begin)
    result = []
    current = [0] * n_digits
    result.append(copy(current))

    while current != [base - 1] * n_digits:
        current[0] += 1
        i = 0

        while current[i] == base:
            current[i] = 0
            i += 1
            current[i] += 1

        result.append(copy(current))

    return [[list_end[n] for n in r] for r in result]


if __name__ == '__main__':
    li = [['a', 'b', 'c'], ['a', 'b', 'c']]
    print(no_duplicate(li))
