"""
Based on: https://www.baeldung.com/java-binary-tree

traverse level order
Based on: https://www.askpython.com/python/examples/level-order-binary-tree
"""

from typing import Optional
from queue import Queue


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def __add_recursive(self, current: Optional[None], value: int) -> Optional[None]:
        if not current:
            return Node(value)

        if value < current.value:
            current.left = self.__add_recursive(current.left, value)
        elif value > current.value:
            current.right = self.__add_recursive(current.right, value)
        else:
            # value already exists
            return current

        return current

    def add(self, value: int) -> None:
        self.root = self.__add_recursive(self.root, value)

    def __contains_node_recursive(self, current: Optional[Node], value: int) -> bool:
        """
        Here we're searching for the value by comparing it to the value in the
        current node; we'll then continue in the left or right child depending
        on the outcome.
        """
        if not current:
            return False
        if value == current.value:
            return True
        return (
            self.__contains_node_recursive(current.left, value)
            if value < current.value
            else self.__contains_node_recursive(current.right, value)
        )

    def contains_node(self, value: int) -> bool:
        return self.__contains_node_recursive(self.root, value)

    def __delete_recursive(self, current: Optional[Node], value: int) -> Optional[None]:
        if not current:
            return None

        if value == current.value:
            # Node to delete found; code to delete the node will go here
            # Once we find the node to delete, there are 3 main different cases:
            # - a node has no children – this is the simplest case; we just need to replace this node with null in its parent node
            if current.left is None and current.right is None:
                return None
            # - a node has exactly one child – in the parent node, we replace this node with its only child.
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left
            # - a node has two children – this is the most complex case because it requires a tree reorganization
            smallest_value = self.__find_smallest_value(current.right)
            current.value = smallest_value
            current.right = self.__delete_recursive(current.right, smallest_value)
            return current

        if value < current.value:
            current.left = self.__delete_recursive(current.left, value)
            return current
        else:
            current.right = self.__delete_recursive(current.right, value)
            return current

    def __find_smallest_value(self) -> int:
        return (
            self.root.value
            if self.root.left is None
            else self.__find_smallest_value(self.root.left)
        )

    def delete_recursive(self, value: int) -> None:
        self.root = self.__delete_recursive(self.root, value)

    def traverse_in_order(self, node: Optional[Node]) -> None:
        """
        Depth-first search is a type of traversal that goes deep as much as
        possible in every child before exploring the next sibling.
        ---
        The in-order traversal consists of first visiting the left sub-tree,
        then the root node, and finally the right sub-tree.
        """
        if node:
            self.traverse_in_order(node.left)
            print(node.value)
            self.traverse_in_order(node.right)

    def traverse_pre_order(self, node: Optional[Node]) -> None:
        """
        Depth-first search is a type of traversal that goes deep as much as
        possible in every child before exploring the next sibling.
        ---
        Pre-order traversal visits first the root node, then the left sub-tree,
        and finally the right sub-tree.
        """
        if node:
            print(node.value)
            self.traverse_in_order(node.left)
            self.traverse_in_order(node.right)

    def traverse_post_order(self, node: Optional[Node]) -> None:
        """
        Depth-first search is a type of traversal that goes deep as much as
        possible in every child before exploring the next sibling.
        ---
        Post-order traversal visits the left sub-tree, the right subt-ree,
        and the root node at the end.
        """
        if node:
            self.traverse_in_order(node.left)
            self.traverse_in_order(node.right)
            print(node.value)

    def traverse_level_order(self, root: Optional[Node]):
        if root is None:
            return

        Q = Queue()
        Q.put(root)  # put an item into the queue
        while not Q.empty():
            node = Q.get()  # remove and return an item from the queue
            if node is None:
                continue
            print(node.value)
            Q.put(node.left)
            Q.put(node.right)


def main() -> None:  # Main function for testing.
    bt = BinaryTree(6)
    bt.add(4)
    bt.add(8)
    bt.add(3)
    bt.add(5)
    bt.add(7)
    bt.add(9)

    print(bt.contains_node(9))
    bt.delete_recursive(9)
    print(bt.contains_node(9))
    bt.add(9)
    print(bt.contains_node(9))

    print("traverse_in_order: ")
    bt.traverse_in_order(bt.root)

    print("traverse_pre_order: ")
    bt.traverse_pre_order(bt.root)

    print("traverse_post_order: ")
    bt.traverse_post_order(bt.root)

    print("traverse_level_order: ")
    bt.traverse_level_order(bt.root)


if __name__ == "__main__":
    main()
