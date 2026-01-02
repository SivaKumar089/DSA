
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

    def cycle_ll():
        slow=fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow== fast:
                return True
        return False


            


# Given list
items = [1, 2, 3, 4, 5]

ll = LinkedList()

for x in items:
    ll.add_end(x)

ll.display()
print(ll.cycle_ll())

