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



def delete_bst(root, data):

    if root is None:
        return None

    if data < root.data:
        root.left = delete_bst(root.left, data)

    elif data > root.data:
        root.right = delete_bst(root.right, data)

    else:
        # case 1 & 2
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # case 3: inorder successor
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete_bst(root.right, temp.data)

    return root


def find_min(node):
    while node.left:
        node = node.left
    return node



def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)
            



arr = [4,1,3,6,8,5]
root = None

for val in arr:
    root = insert_bst(root, val)

result=delete_bst(root,1)

inorder(result)





 
