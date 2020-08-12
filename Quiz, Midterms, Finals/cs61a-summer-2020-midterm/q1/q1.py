email = 'aunghtetpaing@berkeley.edu'

def schedule(treasury, sum_to, max_digit):
    """
    A 'treasury' is a string which contains either digits or '?'s.

    A 'completion' of a treasury is a string that is the same as treasury, except
    with digits replacing each of the '?'s.

    Your task in this question is to find all completions of the given `treasury`
    that use digits up to `max_digit`, and whose digits sum to `sum_to`.

    Note 1: the function int can be used to convert a string to an integer and str
        can be used to convert an integer to a string as such:

        >>> int("5")
        5
        >>> str(5)
        '5'

    Note 2: Indexing and slicing can be used on strings as well as on lists.

        >>> 'evocative'[3]
        'c'
        >>> 'evocative'[3:]
        'cative'
        >>> 'evocative'[:6]
        'evocat'
        >>> 'evocative'[3:6]
        'cat'


    >>> schedule('?????', 25, 5)
    ['55555']
    >>> schedule('???', 5, 2)
    ['122', '212', '221']
    >>> schedule('?2??11?', 5, 3)
    ['0200111', '0201110', '0210110', '1200110']
    """
    def schedule_helper(treasury, sum_sofar, index):
        if sum_sofar==sum_to and any(type(i)==str for i in treasury):
            return [treasury]
        elif sum_to < sum_sofar:
            return []
        elif ______:
            return ______
        ans = []
        for x in max_digit:
            modified_treasury = schedule_helper(treasury,sum([int(i) if type(i) == int else 0 for i in treasury]),x)
            ans+=modified_treasury
        return ans

    return schedule_helper(treasury,0,0)

# ORIGINAL SKELETON FOLLOWS

# def schedule(treasury, sum_to, max_digit):
#     """
#     A 'treasury' is a string which contains either digits or '?'s.

#     A 'completion' of a treasury is a string that is the same as treasury, except
#     with digits replacing each of the '?'s.

#     Your task in this question is to find all completions of the given `treasury`
#     that use digits up to `max_digit`, and whose digits sum to `sum_to`.

#     Note 1: the function int can be used to convert a string to an integer and str
#         can be used to convert an integer to a string as such:

#         >>> int("5")
#         5
#         >>> str(5)
#         '5'

#     Note 2: Indexing and slicing can be used on strings as well as on lists.

#         >>> 'evocative'[3]
#         'c'
#         >>> 'evocative'[3:]
#         'cative'
#         >>> 'evocative'[:6]
#         'evocat'
#         >>> 'evocative'[3:6]
#         'cat'


#     >>> schedule('?????', 25, 5)
#     ['55555']
#     >>> schedule('???', 5, 2)
#     ['122', '212', '221']
#     >>> schedule('?2??11?', 5, 3)
#     ['0200111', '0201110', '0210110', '1200110']
#     """
#     def schedule_helper(treasury, sum_sofar, index):
#         if ______ and ______:
#             return [treasury]
#         elif ______:
#             return []
#         elif ______:
#             return ______
#         ans = []
#         for x in ______:
#             modified_treasury = ______
#             ______
#         return ans

#     return ______
