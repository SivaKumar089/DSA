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

result=[]
def bst_path(root,path):

    if not root:
        return

    path+=str(root.data)

    if not root.left and  not root.right:
        result.append(path)
        return
    
    path+="->"

    bst_path(root.left,path)
    bst_path(root.right,path)

    
    return result


    


arr=[4,2,7,1,3,6,9]

root=add_tree(arr)
print(bst_path(root,""))

# inorder(root)