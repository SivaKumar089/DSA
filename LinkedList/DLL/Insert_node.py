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

    # Print DLL
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")


items = [1, 2, 4, 5]

ll = LinkedList()

for x in items:
    ll.add_end(x)

ll.print_list()
