
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

    def remove_dublicate(self):
        if not self.head or not self.head.next:
            return
        
        seen=set()
        current=self.head
        prev=None

        
        while current:
            if current.data in seen:
                prev.next=current.next
            else:
                seen.add(current.data)
                prev=current
            current=current.next



            


# Given list
items = [1, 2, 3, 4,1, 5]

ll = LinkedList()

for x in items:
    ll.add_end(x)

ll.display()

ll.remove_dublicate()



ll.display()