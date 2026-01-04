class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None





def insert_tree(root,data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left=insert_tree(root.left,data)
    else:
        root.right=insert_tree(root.right,data)

    return root


def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.data,end=' ')
    inorder(root.right)


def min_value(root):
    if root is None:
        return None

    if root.left is not None:
        return min_value(root.left)

    return root.data


def max_value(root):

    if root is None:
        return
    
    if root.right is not None:
        return max_value(root.right)

    return root.data

arr=[5,7,8,3,2,4,9]
root=None



for num in arr:
    root=insert_tree(root,num)


inorder(root)
print('min:')
print(min_value(root),end=' ')
print('max:')
print(max_value(root),end=' ')



