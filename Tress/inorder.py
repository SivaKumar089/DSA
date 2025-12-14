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


arr=[1,2,3,4,5]

root=add_tree(arr)


inorder(root)