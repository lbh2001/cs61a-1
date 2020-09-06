email = 'aunghtetpaing@berkeley.edu'

"""
This question is in two parts, implementing `similarizer` and
    `smallest_without_penalty`. See the specifications above each definition for
    details.

You can do the parts in any order, the tests for part (b) do not rely on
    part (a) being completed.
"""

"""
Part (a)
"""
def similarizer(t, atmosphere):
    """
    Given a tree `t` and a non-negative integer `atmosphere`, write a function
        `similarizer` that mutates the given tree so that every root-to-leaf
        path is of depth `atmosphere`.

    If you need to add nodes add a tree node with label "penalty" to the correct leaf
    If you need to remove nodes simply truncate excess nodes.

    NOTE: Remember that depth is 0 indexed. That means that if `atmosphere=2`
        each path's length is going to be 3.

    To run tests just for this part, run
        python3 ok -q a

    >>>> t1 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])]), Tree(5)])
    >>>> print(t1)
    1
        2
            3
                4
        5
    >>>> similarizer(t1, 2)
    >>>> print(t1)
    1
        2
            3
        5
            penalty

    >>>> t2 = Tree(4, [Tree(5, [Tree(6), Tree(7)]), Tree(10), Tree(15, [Tree(16, [Tree(17, [Tree(18, [Tree(19)])])])])])
    >>>> similarizer(t2, 3)
    >>>> print(t2)
    4
        5
            6
                penalty
            7
                penalty
        10
            penalty
                penalty
        15
            16c
                17
    """
    if atmosphere == 0:
        t.branches = []
    elif t.is_leaf():
        t.branches = [Tree('penalty')]
    for branch in t.branches:
        similarizer(branch, atmosphere-1)

"""
Part (b)
"""
def smallest_without_penalty(t):
    """
    Given the `similarizer`'d Tree `t`, find the shortest root-to-leaf path of
    the original tree.

    That is the shortest path that does not include added "penalty" nodes. If
    there are multiple shortest paths, you can return any of the shortest
    paths.

    You do not have to worry about the case where every path of the original
    tree has been truncated.

    To run tests just for this part, run
        python3 ok -q b

    >>>> t1 = Tree(1, [Tree(2, [Tree(3)]), Tree(5, [Tree("penalty")])])
    >>>> print(t1)
    1
        2
            3
        5
            penalty
    >>>> smallest_without_penalty(t1)
    [1, 5]

    >>>> t2 = Tree(4, [Tree(5, [Tree(6, [Tree("penalty")]), Tree(7, [Tree("penalty")])]), Tree(10, [Tree("penalty", [Tree("penalty")])]), Tree(15, [Tree(16, [Tree(17)])])])
    >>>> print(t2)
    4
        5
            6
                penalty
            7
                penalty
        10
            penalty
                penalty
        15
            16
                17
    >>>> smallest_without_penalty(t2)
    [4, 10]
    """
    if all([b.label == 'penalty' for b in t.branches] + [t.is_leaf()]):
        return [t.label]
    return [t.label] + min( [smallest_without_penalty(b) for b in t.branches], key=lambda x: len(x))

class Tree:
    """
    >>>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>>> t.label
    3
    >>>> t.branches[0].label
    2
    >>>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = ' ' * (4 * indent) + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

# ORIGINAL SKELETON FOLLOWS

# """
# This question is in two parts, implementing `similarizer` and
#     `smallest_without_penalty`. See the specifications above each definition for
#     details.

# You can do the parts in any order, the tests for part (b) do not rely on
#     part (a) being completed.
# """

# """
# Part (a)
# """
# def similarizer(t, atmosphere):
#     """
#     Given a tree `t` and a non-negative integer `atmosphere`, write a function
#         `similarizer` that mutates the given tree so that every root-to-leaf
#         path is of depth `atmosphere`.

#     If you need to add nodes add a tree node with label "penalty" to the correct leaf
#     If you need to remove nodes simply truncate excess nodes.

#     NOTE: Remember that depth is 0 indexed. That means that if `atmosphere=2`
#         each path's length is going to be 3.

#     To run tests just for this part, run
#         python3 ok -q a

#     >>>> t1 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])]), Tree(5)])
#     >>>> print(t1)
#     1
#         2
#             3
#                 4
#         5
#     >>>> similarizer(t1, 2)
#     >>>> print(t1)
#     1
#         2
#             3
#         5
#             penalty

#     >>>> t2 = Tree(4, [Tree(5, [Tree(6), Tree(7)]), Tree(10), Tree(15, [Tree(16, [Tree(17, [Tree(18, [Tree(19)])])])])])
#     >>>> similarizer(t2, 3)
#     >>>> print(t2)
#     4
#         5
#             6
#                 penalty
#             7
#                 penalty
#         10
#             penalty
#                 penalty
#         15
#             16
#                 17
#     """
#     if ______:
#         t.branches = []
#     elif ______:
#         t.branches = ______
#     for ______ in ______:
#         ______

# """
# Part (b)
# """
# def smallest_without_penalty(t):
#     """
#     Given the `similarizer`'d Tree `t`, find the shortest root-to-leaf path of
#     the original tree.

#     That is the shortest path that does not include added "penalty" nodes. If
#     there are multiple shortest paths, you can return any of the shortest
#     paths.

#     You do not have to worry about the case where every path of the original
#     tree has been truncated.

#     To run tests just for this part, run
#         python3 ok -q b

#     >>>> t1 = Tree(1, [Tree(2, [Tree(3)]), Tree(5, [Tree("penalty")])])
#     >>>> print(t1)
#     1
#         2
#             3
#         5
#             penalty
#     >>>> smallest_without_penalty(t1)
#     [1, 5]

#     >>>> t2 = Tree(4, [Tree(5, [Tree(6, [Tree("penalty")]), Tree(7, [Tree("penalty")])]), Tree(10, [Tree("penalty", [Tree("penalty")])]), Tree(15, [Tree(16, [Tree(17)])])])
#     >>>> print(t2)
#     4
#         5
#             6
#                 penalty
#             7
#                 penalty
#         10
#             penalty
#                 penalty
#         15
#             16
#                 17
#     >>>> smallest_without_penalty(t2)
#     [4, 10]
#     """
#     if all(______):
#         return [t.label]
#     return ______ + min(______, key=______)

# class Tree:
#     """
#     >>>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
#     >>>> t.label
#     3
#     >>>> t.branches[0].label
#     2
#     >>>> t.branches[1].is_leaf()
#     True
#     """
#     def __init__(self, label, branches=[]):
#         for b in branches:
#             assert isinstance(b, Tree)
#         self.label = label
#         self.branches = list(branches)

#     def is_leaf(self):
#         return not self.branches

#     def __str__(self):
#         def print_tree(t, indent=0):
#             tree_str = ' ' * (4 * indent) + str(t.label) + "\n"
#             for b in t.branches:
#                 tree_str += print_tree(b, indent + 1)
#             return tree_str
#         return print_tree(self).rstrip()
