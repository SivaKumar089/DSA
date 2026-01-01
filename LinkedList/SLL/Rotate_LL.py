class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):      
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    

    def rotate_ll(self,k):
        if not self.head or not self.head.next or k == 0:
            return self.head
        
        length = 1
        tail = self.head
        while tail.next:
            tail = tail.next
            length += 1
        
        tail.next = self.head
        
        k = k % length
        steps_to_new_tail = length - k
        
        new_tail = self.head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head



# Given list
items = [1, 2, 3, 4, 5]

ll = LinkedList()

for x in items:
    ll.add_end(x)

print("Before Rotation:")
ll.display()

ll.head = ll.rotate_ll(2)

print("After Rotation:")
ll.display()
