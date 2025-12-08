
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

    def add_node(self, index, data):

        new = Node(data)

        # Case 1: Add at start
        if index == 0:
            new.next = self.head
            self.head = new
            return

        temp = self.head
        i = 0

        # Traverse to (index - 1) node
        while temp is not None:
            if i + 1 == index:   # found previous node
                new.next = temp.next
                temp.next = new
                return

            temp = temp.next
            i += 1

        return -1   # index out of range







# Given list
items = [1, 2, 4, 5]

ll = LinkedList()

for x in items:
    ll.add_end(x)

ll.display()

ll.add_node(0,3)

ll.display()

