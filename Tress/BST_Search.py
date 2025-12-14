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



def search_bst(root,data):
    
    if root is None:
        return 0

    if root.data == data:
        return root
    elif root.data > data:
      return  search_bst(root.left,data)
    else:
        return search_bst(root.right,data)
            



arr = [4,1,3,6,8,5]
root = None

for val in arr:
    root = insert_bst(root, val)

result=search_bst(root,10)
print("found" if result else "not found")


 
