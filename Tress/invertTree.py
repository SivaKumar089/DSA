class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    

def add_tree(arr,i=0):
    
    if i>= len(arr):
        return None
    
    root=Node(arr[i])
    root.left=add_tree(arr,2*i+1)
    root.right=add_tree(arr,2*i+2)

    return root

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)


def invertTree(root):
    if root is None:
        return None

        # swap children
    root.left, root.right = root.right, root.left

        # recursive calls
    invertTree(root.left)
    invertTree(root.right)

    return root

arr=[4,2,7,1,3,6,9]

root=add_tree(arr)

root=invertTree(root)

inorder(root)