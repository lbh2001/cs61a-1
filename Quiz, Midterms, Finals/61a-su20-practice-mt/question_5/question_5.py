

#    Definitions. A trictionary is a pair of Tree instances k and v that have identical structure: each node in k
#    has a corresponding node in v. The labels in k are called keys. Each key may be the label for multiple nodes
#    in k, and the values for that key are the labels of all the corresponding nodes in v.
#    A lookup function returns one of the values for a key. Specifically, a lookup function for a node in k is a function
#    that takes v as an argument and returns the label for the corresponding node in v.
#    Implement the generator function lookups, which takes a Tree instance k and some key. It yields all lookup
#    functions for nodes in k that have key as their label. The new_lookup function is part of the implementation.
#
#       k:                        v:                             key:     value:
#                  5                         'Go'                 2        'C', 'A'
#               /  |  \                    /   |  \               3        'S'
#             7    8    5               'C'   'A'  'L'            4         6, 1
#            /   / |    | \             /    / |    | \           5        'Go', 'L'
#           2   3  4    4  2          'C'  'S' 6    1 'A'         7        'C'
#                                                                 8        'A'
#

def lookups(k, key):
    """Yield one lookup function for each node of k that has the label key.
    >>> k = Tree(5, [Tree(7, [Tree(2)]), Tree(8, [Tree(3), Tree(4)]), Tree(5, [Tree(4), Tree(2)])])
    >>> v = Tree('Go', [Tree('C', [Tree('C')]), Tree('A', [Tree('S'), Tree(6)]), Tree('L', [Tree(1), Tree('A')])])        
    >>> [f(v) for f in lookups(k, 2)]
    ['C', 'A']
    >>> [f(v) for f in lookups(k, 3)]
    ['S']
    >>> [f(v) for f in lookups(k, 6)]
    []
    """
    if ______:
        yield lambda v: ______
    for i in range(len(k.branches)):
        for ______ in ______:
            yield new_lookup(i, lookup)
def new_lookup(i, f):
    def g(v):
        return ______
    return g


### Tree Class definition ###
class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

# ORIGINAL SKELETON FOLLOWS


# #    Definitions. A trictionary is a pair of Tree instances k and v that have identical structure: each node in k
# #    has a corresponding node in v. The labels in k are called keys. Each key may be the label for multiple nodes
# #    in k, and the values for that key are the labels of all the corresponding nodes in v.
# #    A lookup function returns one of the values for a key. Specifically, a lookup function for a node in k is a function
# #    that takes v as an argument and returns the label for the corresponding node in v.
# #    Implement the generator function lookups, which takes a Tree instance k and some key. It yields all lookup
# #    functions for nodes in k that have key as their label. The new_lookup function is part of the implementation.
# #
# #       k:                        v:                             key:     value:
# #                  5                         'Go'                 2        'C', 'A'
# #               /  |  \                    /   |  \               3        'S'
# #             7    8    5               'C'   'A'  'L'            4         6, 1
# #            /   / |    | \             /    / |    | \           5        'Go', 'L'
# #           2   3  4    4  2          'C'  'S' 6    1 'A'         7        'C'
# #                                                                 8        'A'
# #

# def lookups(k, key):
#     """Yield one lookup function for each node of k that has the label key.
#     >>> k = Tree(5, [Tree(7, [Tree(2)]), Tree(8, [Tree(3), Tree(4)]), Tree(5, [Tree(4), Tree(2)])])
#     >>> v = Tree('Go', [Tree('C', [Tree('C')]), Tree('A', [Tree('S'), Tree(6)]), Tree('L', [Tree(1), Tree('A')])])        
#     >>> [f(v) for f in lookups(k, 2)]
#     ['C', 'A']
#     >>> [f(v) for f in lookups(k, 3)]
#     ['S']
#     >>> [f(v) for f in lookups(k, 6)]
#     []
#     """
#     if ______:
#         yield lambda v: ______
#     for i in range(len(k.branches)):
#         for ______ in ______:
#             yield new_lookup(i, lookup)
# def new_lookup(i, f):
#     def g(v):
#         return ______
#     return g


# ### Tree Class definition ###
# class Tree:
#     def __init__(self, label, branches=[]):
#         self.label = label
#         for branch in branches:
#             assert isinstance(branch, Tree)
#         self.branches = list(branches)

#     def is_leaf(self):
#         return not self.branches
