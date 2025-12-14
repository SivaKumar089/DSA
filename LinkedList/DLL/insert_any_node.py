class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at end
    def add_end(self, data):
        new_node = Node(data)

        # First node
        if self.head is None:
            self.head = new_node
            return

        # Move to last node
        temp = self.head
        while temp.next:
            temp = temp.next

        # Link new node
        temp.next = new_node
        new_node.prev = temp


    def add_any_node(self,data,index):

        new_node=Node(data)

        if index==0:
            temp=self.head
            temp.prev=new_node
            new_node.next=temp
            self.head = new_node
            return

        temp=self.head

        i=0

        while temp is not None:

            if i+1 == index:
                new_node.next=temp.next
                temp.next=new_node
                temp.next.prev=new_node
                new_node.prev=temp

                return
            
            temp=temp.next
            i+=1
        return -1    
                
    # Print- DLL
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


items = [ 2, 3, 4, 5]

ll = LinkedList()

for x in items:
    ll.add_end(x)

ll.print_list()

ll.add_any_node(7,2)

ll.print_list()
