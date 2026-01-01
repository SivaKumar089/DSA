
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

    def Palindrome(self):
        if not self.head or not self.head.next:
            return True
        
        slow=self.head
        fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        curr=slow

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        
        first=self.head
        second=prev


        while second:

            if first.data != second.data:
                return False
            first=first.next
            second=second.next
        return True
    
            

        

    

# Given list
items = [1, 2,1]

ll = LinkedList()

for x in items:
    ll.add_end(x)
print(ll.Palindrome())
# ll.display()


