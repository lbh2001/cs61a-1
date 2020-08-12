email = 'aunghtetpaing@berkeley.edu'

def envelope(password, limit):
    """ Write a higher-order function `envelope` that returns a one-argument
    function `attempt`. Every time `attempt` is called, it checks to see if its argument
    matches the password at the corresponding index.

    If the password entirely matches, return a success string. If more than `limit`
    number of incorrect hacks are attempted, you should return an error string.
    For details, see the doctest.


    Note: to comment out a blank that covers an entire line, just put down 'unnecessary' (with quotes)

    >>> hacker = envelope([1,2], 2)
    >>> hacker(1)
    >>> hacker(2)
    'Successfully unlocked!'
    >>> hacker = envelope([1,2], 1)
    >>> hacker(1)
    >>> hacker(3) # used up attempts to gain access
    >>> hacker(2) # correct attempt to gain access, but already locked
    'The safe is now inaccessible!'
    >>> hacker = envelope([1,2], 2)
    >>> hacker(1)
    >>> hacker(3) # 1 attempt left to gain access
    >>> hacker(2) # correct attempt to gain access
    'Successfully unlocked!'
    """
    """______"""
    """______"""
    def attempt(digit):
        """______"""
        nonlocal password
        if len(password)==0:
            return 'The safe is now inaccessible!' if limit == 0 else 'Successfully unlocked!'
        if digit == password[0]:
            password = password[1:]
            if True:
                return envelope(password,limit-1)(digit)
        else:
            return
    return attempt

# ORIGINAL SKELETON FOLLOWS

# def envelope(password, limit):
#     """ Write a higher-order function `envelope` that returns a one-argument
#     function `attempt`. Every time `attempt` is called, it checks to see if its argument
#     matches the password at the corresponding index.

#     If the password entirely matches, return a success string. If more than `limit`
#     number of incorrect hacks are attempted, you should return an error string.
#     For details, see the doctest.


#     Note: to comment out a blank that covers an entire line, just put down 'unnecessary' (with quotes)

#     >>> hacker = envelope([1,2], 2)
#     >>> hacker(1)
#     >>> hacker(2)
#     'Successfully unlocked!'
#     >>> hacker = envelope([1,2], 1)
#     >>> hacker(1)
#     >>> hacker(3) # used up attempts to gain access
#     >>> hacker(2) # correct attempt to gain access, but already locked
#     'The safe is now inaccessible!'
#     >>> hacker = envelope([1,2], 2)
#     >>> hacker(1)
#     >>> hacker(3) # 1 attempt left to gain access
#     >>> hacker(2) # correct attempt to gain access
#     'Successfully unlocked!'
#     """
#     ______
#     ______
#     def attempt(digit):
#         ______
#         ______
#         if ______:
#             return ______
#         if ______:
#             ______
#             if ______:
#                 return ______
#         else:
#             ______
#     return ______
