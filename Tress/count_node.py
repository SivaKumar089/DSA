class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_bst(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert_bst(root.left, data)
    else:
        root.right = insert_bst(root.right, data)

    return root


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


arr = [4, 1, 3, 6, 8, 5]
root = None

for val in arr:
    root = insert_bst(root, val)

print("Total nodes in BST:", count_nodes(root))

