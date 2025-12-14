
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

        
    def remove_node(self,data):
        temp=self.head

        while temp is not None:
        
            if temp.next.data == data:
                temp.next=temp.next.next
                temp.next.next=temp
                return
            

            temp=temp.next
        return -1


# Given list
items = [1, 2, 3, 4, 5]

ll = LinkedList()

for x in items:
    ll.add_end(x)

ll.display()

ll.remove_node(4)

ll.display()


