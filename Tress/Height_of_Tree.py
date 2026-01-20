from collections import deque
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



def height(root):
    if root is None:
        return 0

    q = deque([root])
    depth = 0

    # Loop until the queue is empty
    while q:
        levelSize = len(q)

        # Traverse all nodes at the current level
        for _ in range(levelSize):
            curr = q.popleft()

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        # Increment depth after traversing each level
        depth += 1

    return depth - 1
            



arr = [4,2,3,1,7,5,6]
root = None

for val in arr:
    root = insert_bst(root, val)

print(height(root))