"""
    disjoint set
    Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    Reference: https://github.com/TheAlgorithms/Python/blob/master/data_structures/disjoint_set/disjoint_set.py
"""

from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data


def make_set(x: Node):
    """
    make x as a set.
    """
    # rank is the distance from x to its' parent
    # root's rank is 0
    x.rank = 0
    x.parent = x


def find_set(x: Node):
    """
    return the parent of x
    """
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def union_set(x: Node, y: Node):
    """
    union two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.
    """
    x, y = find_set(x), find_set(y)
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def main():
    set_1 = Node(1)
    set_2 = Node(2)
    make_set(set_1)
    make_set(set_2)
    print("set_1.parent: ", find_set(set_1))
    print("set_2.parent: ", find_set(set_2))
    print("set_1.rank: ", set_1.rank)
    print("set_2.rank: ", set_2.rank)

    union_set(set_1, set_2)
    print("set_1.rank: ", set_1.rank)
    print("set_2.rank: ", set_2.rank)


if __name__ == "__main__":
    main()
