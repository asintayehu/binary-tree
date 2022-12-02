class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        """
        :param traversal_type: str parameter that specifies type of traversal
        :return:
        """
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        else:
            return f"traversal type {traversal_type} is not supported"

    def preorder_print(self, start, traversal):
        """
        Root -> Left Subtree -> Right Subtree
        :param start: node that will be updated during every recursive call
        :param traversal: node that will be printed out, will be updated
        :return: traversal
        """
        if start is not None:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal





#          1
#      /       \
#     2         3
#    /   \     /  \
#   4     5   6    7

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
# 1-2-4-5-3-6-7-

