email = 'aunghtetpaing@berkeley.edu'

def subdrama(cell):
    """
    A 'drama' is a sequence of digits of length `d` composed entirely of the digit `d`. Examples include
        1
        4444
        7777777

    Note that `1 <= d <= 9`; there are no 0-length dramas.

    Your task is to implement the `subdrama` function, which takes in an integer `cell` and returns
        whether `cell` contains a drama as a consecutive subinteger of its digits.

    >>> subdrama(2233) # 22 counts
    True
    >>> subdrama(2444423) # 4444 counts
    True
    >>> subdrama(82223) # 22 counts even if it appears as part of 222
    True
    >>> subdrama(234562) # 2...2 does not count if the 2s are not consecutive
    False
    >>> subdrama(1) # 1 counts
    True
    >>> subdrama(498729879871) # 1 counts
    True
    >>> subdrama(149872987987) # 1 counts
    True
    >>> subdrama(4445555) # no dramas in this number
    False
    >>> subdrama(20) # no dramas in this number
    False
    """
    current_digit = cell%10
    count = 0
    while cell:
        last = current_digit
        if last == cell % 10:
            count += 1
        else:
            count = 1
            current_digit = cell %10
        if count == current_digit:
            return True
        cell = cell//10
    return False

# ORIGINAL SKELETON FOLLOWS

# def subdrama(cell):
#     """
#     A 'drama' is a sequence of digits of length `d` composed entirely of the digit `d`. Examples include
#         1
#         4444
#         7777777

#     Note that `1 <= d <= 9`; there are no 0-length dramas.

#     Your task is to implement the `subdrama` function, which takes in an integer `cell` and returns
#         whether `cell` contains a drama as a consecutive subinteger of its digits.

#     >>> subdrama(2233) # 22 counts
#     True
#     >>> subdrama(2444423) # 4444 counts
#     True
#     >>> subdrama(82223) # 22 counts even if it appears as part of 222
#     True
#     >>> subdrama(234562) # 2...2 does not count if the 2s are not consecutive
#     False
#     >>> subdrama(1) # 1 counts
#     True
#     >>> subdrama(498729879871) # 1 counts
#     True
#     >>> subdrama(149872987987) # 1 counts
#     True
#     >>> subdrama(4445555) # no dramas in this number
#     False
#     >>> subdrama(20) # no dramas in this number
#     False
#     """
#     current_digit = ______
#     count = ______
#     while ______:
#         last = ______
#         if ______:
#             count += 1
#         else:
#             count = ______
#             ______
#         if ______:
#             ______
#         cell = ______
#     return ______
