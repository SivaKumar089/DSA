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

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=' ')


arr=[1,2,3,4,5]

root=add_tree(arr)


postorder(root)