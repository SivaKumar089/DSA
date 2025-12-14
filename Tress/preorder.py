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

def preorder(root):
    if not root:
        return
    print(root.data,end=' ')
    preorder(root.left)
    preorder(root.right)


arr=[1,2,3,4,5]

root=add_tree(arr)


preorder(root)










# def print_tree(root, space=0, level_gap=10):
#     if root is None:
#         return
    
#     space += level_gap
    
#     print_tree(root.right, space)
    
#     print()
#     print(" " * (space - level_gap) + str(root.value))
    
#     print_tree(root.left, space)
