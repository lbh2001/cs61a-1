email = 'aunghtetpaing@berkeley.edu'

def elevator(speech, coffee):
    """
    Write a function `elevator` that takes in two lists.
        `speech` is a list of strings
        `coffee` is a list of integers

    It returns a new list where every element from `speech` is copied the
    number of times as the corresponding element in `coffee`. If the number
    of times to be copied is negative (-k), then it removes the previous
    k elements added.

    Note 1: `speech` and `coffee` do not have to be the same length, simply ignore
    any extra elements in the longer list.

    Note 2: you can assume that you will never be asked to delete more
    elements than exist


    >>> elevator(['a', 'b', 'c'], [1, 2, 3])
    ['a', 'b', 'b', 'c', 'c', 'c']
    >>> elevator(['a', 'b', 'c'], [3])
    ['a', 'a', 'a']
    >>> elevator(['a', 'b', 'c'], [0, 2, 0])
    ['b', 'b']
    >>> elevator([], [1,2,3])
    []
    >>> elevator(['a', 'b', 'c'], [1, -1, 3])
    ['c', 'c', 'c']
    """
    def elevator_helper(s, coffee, index):
        if not len(speech) or index == len(coffee):
            return s
        if coffee[index]>=0:
            s += [speech[index]]*coffee[index]
        else:
            s = s[:coffee[index]]
        return elevator_helper(s, coffee, index+1)
    return elevator_helper([],coffee,0)

# ORIGINAL SKELETON FOLLOWS

# def elevator(speech, coffee):
#     """
#     Write a function `elevator` that takes in two lists.
#         `speech` is a list of strings
#         `coffee` is a list of integers

#     It returns a new list where every element from `speech` is copied the
#     number of times as the corresponding element in `coffee`. If the number
#     of times to be copied is negative (-k), then it removes the previous
#     k elements added.

#     Note 1: `speech` and `coffee` do not have to be the same length, simply ignore
#     any extra elements in the longer list.

#     Note 2: you can assume that you will never be asked to delete more
#     elements than exist


#     >>> elevator(['a', 'b', 'c'], [1, 2, 3])
#     ['a', 'b', 'b', 'c', 'c', 'c']
#     >>> elevator(['a', 'b', 'c'], [3])
#     ['a', 'a', 'a']
#     >>> elevator(['a', 'b', 'c'], [0, 2, 0])
#     ['b', 'b']
#     >>> elevator([], [1,2,3])
#     []
#     >>> elevator(['a', 'b', 'c'], [1, -1, 3])
#     ['c', 'c', 'c']
#     """
#     def elevator_helper(______, ______, ______):
#         if ______:
#             return ______
#         if ______:
#             ______ = ______
#         else:
#             ______ = ______[:______]
#         return ______
#     return ______
