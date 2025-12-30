class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head=None
    

    def insert_node(self,data):
        newNode=Node(data)

        if self.head is None:
            self.head=newNode
            newNode.next=newNode
            newNode.prev=newNode
        else:
            tail=self.head.prev
            tail.next=newNode
            newNode.prev=tail
            newNode.next=self.head
            self.head.prev=newNode


    def display(self):

        if self.head is None:
            print("Empty")
        temp=self.head
        while True:
            print(temp.data)
            temp=temp.next
            if temp== self.head:
                break
            
arr = [1,2,3,4,5]

CLL=CircularDoublyLinkedList()


for num in arr:
    CLL.insert_node(num)

CLL.display()