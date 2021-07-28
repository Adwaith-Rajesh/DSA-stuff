# resource
# https://www.youtube.com/watch?v=6oL-0TdVy28
# https://docs.google.com/presentation/d/1OPqeIRnRyYLpFQPk7Wf0qmCUe-cMmAsI1hUqpab0B_s/edit#slide=id.g35174c1207_0_13


class Node:

    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"({self.data} {self.left} {self.right})"


class BinaryTree:

    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")

    def preorder_print(self, start, traversal):
        """
        1. Check if the current node is empty / null.
        2. Display the data part of the root (or current node).
        3. Traverse the left subtree by recursively calling the pre-order function.
        4. Traverse the right subtree by recursively calling the pre-order function
        """

        if start:
            traversal += str(start.data) + "-"
            # print(start)
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)

        return traversal

    def inorder_print(self, start, traversal):
        """
        left -> root -> right
        1. Check if the current node is empty / null.
        2. Traverse the left subtree by recursively calling the in-order function.
        3. Display the data part of the root (or current node).
        4. Traverse the right subtree by recursively calling the in-order function.
        """

        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.data) + "-"
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left -> Right -> Root"""

        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.data) + "-"
        return traversal


#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6   7

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
