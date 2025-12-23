class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


def insert_bst(root,data):
    
    if root is None:
        return Node(data)
    
    
    if root.data > data:
        root.left=insert_bst(root.left,data)
    else:
        root.right=insert_bst(root.right,data)

    return root        






arr = [4,1,3,6,8,5]
root = None

for val in arr:
    root = insert_bst(root, val)




