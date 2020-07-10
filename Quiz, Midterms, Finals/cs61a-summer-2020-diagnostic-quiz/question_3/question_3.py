email = 'aunghtetpaing@berkeley.edu'

def falconer(semicolon, k):
    """
    Given a number `semicolon`, finds the largest number of length `k` or fewer,
    composed of digits from `semicolon`, in order.

    >>> falconer(1234, 1)
    4
    >>> falconer(32749, 2)
    79
    >>> falconer(1917, 2)
    97
    >>> falconer(32749, 18)
    32749
    """
    if len(str(semicolon)) <= k:
        return semicolon
    a = [int(x) for x in str(semicolon)]
    b = [x for x in a if not x == min(a)]
    return falconer(int(''.join(str(x) for x in b)),k)

# ORIGINAL SKELETON FOLLOWS

# def falconer(semicolon, k):
#     """
#     Given a number `semicolon`, finds the largest number of length `k` or fewer,
#     composed of digits from `semicolon`, in order.
#
#     >>> falconer(1234, 1)
#     4
#     >>> falconer(32749, 2)
#     79
#     >>> falconer(1917, 2)
#     97`
#     >>> falconer(32749, 18)
#     32749
#     """
#     if ______:
#         return ______
#     a = ______
#     b = ______
#     return ______
