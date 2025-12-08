
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

    def sum_of_node(self):
        
        sum=0       # Sum of Node
        # count=0   # Count the node
        temp=self.head

        while temp is not None:
            sum+=temp.data        # Sum of node

            # count+=1            # Count of mnode

            temp=temp.next
        print(sum)




# Given list
items = [1, 2, 3, 4, 5]

ll = LinkedList()

for x in items:
    ll.add_end(x)

ll.display()

ll.sum_of_node()




