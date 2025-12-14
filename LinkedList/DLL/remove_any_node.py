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


    def remove_any_node(self, data):
        temp = self.head

        # Case 1: list empty
        if temp is None:
            return -1

        # Case 2: delete the head node
        if temp.data == data:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        # Case 3: delete any middle / last node
        while temp is not None:
            if temp.data == data:

                # Stitch previous node to next node
                if temp.prev:
                    temp.prev.next = temp.next

                if temp.next:
                    temp.next.prev = temp.prev

                return  # deletion successful

            temp = temp.next

        return -1  # not found

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

ll.remove_any_node(4)

ll.print_list()
