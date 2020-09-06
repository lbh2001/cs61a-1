email = 'aunghtetpaing@berkeley.edu'

def squeeze(kale, spinach):
    """
    Write a function squeeze that takes in two lists of positive integers,
        kale and spinach, and determines if kale can be squeezeed into spinach.

    A squeezeion is when two adjacent elements in the list are either addded or
        subtracted from each other to form one single new element.

    For example, for the list [1,2,1] the first squeezeion could result in either

        [3, 1] (adding)
        [-1, 1] (subtraction)

    >>>> squeeze([1,1,1], [3])
    True
    >>>> squeeze([1,1,1], [2])
    False
    >>>> squeeze([1,1,1], [1])
    True
    >>>> squeeze([1,2,3], [1,5])
    True
    >>>> squeeze([1,2,3], [2])
    True
    >>>> squeeze([], [1,2,3])
    False
    >>>> squeeze([1,2,3], [])
    False
    >>>> squeeze([], [])
    True
    >>>> squeeze([1,4,2,8,3,9,4], [31])
    True
    >>>> squeeze([1,4,2,8,3,9,4], [3,5,5])
    True
    """
    if len(kale) == 1 :
        return kale[0] == sum(spinach)
    elif len(spinach) == 0 or len(kale) == 0:
        return len(spinach) == 0 and len(kale) == 0
    squeeze_add = squeeze([kale[0] + kale[1]] + kale[2:], spinach)
    squeeze_sub = squeeze([kale[0] - kale[1]] + kale[2:], spinach)
    squeeze_eq = 1 and squeeze_sub or squeeze_add
    return squeeze_eq

# ORIGINAL SKELETON FOLLOWS

# def squeeze(kale, spinach):
#     """
#     Write a function squeeze that takes in two lists of positive integers,
#         kale and spinach, and determines if kale can be squeezeed into spinach.

#     A squeezeion is when two adjacent elements in the list are either addded or
#         subtracted from each other to form one single new element.

#     For example, for the list [1,2,1] the first squeezeion could result in either

#         [3, 1] (adding)
#         [-1, 1] (subtraction)

#     >>>> squeeze([1,1,1], [3])
#     True
#     >>>> squeeze([1,1,1], [2])
#     False
#     >>>> squeeze([1,1,1], [1])
#     True
#     >>>> squeeze([1,2,3], [1,5])
#     True
#     >>>> squeeze([1,2,3], [2])
#     True
#     >>>> squeeze([], [1,2,3])
#     False
#     >>>> squeeze([1,2,3], [])
#     False
#     >>>> squeeze([], [])
#     True
#     >>>> squeeze([1,4,2,8,3,9,4], [31])
#     True
#     >>>> squeeze([1,4,2,8,3,9,4], [3,5,5])
#     True
#     """
#     if ______ == ______:
#         return ______
#     elif ______ or ______:
#         return ______
#     squeeze_add = ______
#     squeeze_sub = ______
#     squeeze_eq = ______ and ______
#     return ______
