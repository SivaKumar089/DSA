
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class CircularLL:
    def __init__(self):
        self.head=None

    def insert_node(self,data):
        new=Node(data)

        if not self.head:
            self.head=new
            new.next=self.head
            return
        
        temp=self.head

        while temp.next != self.head:
            temp=temp.next
        temp.next=new
        new.next=self.head

    def del_first(self):

        if not self.head:
            return
        
        temp=self.head

        if temp.next == self.head:
            self.head=None
            return
        
        while temp.next!= self.head:
            temp=temp.next
        
        temp.next=self.head.next
        self.head=self.head.next
        

    def display(self):

        if not self.head:
            print('empty')
            return
        
        temp=self.head

        while True:
            print(temp.data,end="-> ")
            temp=temp.next

            if temp==self.head:
                break   
        print('Back to Head')
    

arr=[1,2,3,4,5]

Cl=CircularLL()

for num in arr:
    Cl.insert_node(num)

Cl.display()
Cl.del_first()
Cl.display()




