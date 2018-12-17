from functools import reduce
from random import randint


class HighestProduct:
    """
    This is simple "one-line" solution.
    Execution time for array with 1000000 elements is 0.144365s
    """
    @staticmethod
    def calculate1(values=[], count=3):
        if len(values) is 0:
            return 0
        return reduce((lambda x, y: x * y),
                      sorted(values, reverse=True)[0:count])

    """
    This is slightly ugly, but more faster solution.
    Execution time for array with 1000000 elements is 0.051094s
    """
    @staticmethod
    def calculate2(values=[], count=3):
        if len(values) is 0:
            return 0
        heighest = values[0:count]
        minimum = min(heighest)
        for val in values[count:]:
            if val > minimum:
                heighest.append(val)
                heighest = sorted(heighest, reverse=True)[0:count]
                minimum = min(heighest)
        return reduce((lambda x, y: x * y), heighest)

