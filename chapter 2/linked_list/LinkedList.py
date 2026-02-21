from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def remove(self, item):
        if self.head is None:
            return

        if self.head.data == item:
            self.head = self.head.next
            return

        current = self.head

        while current.next:
            if current.next.data == item:
                current.next = current.next.next
                return
            current = current.next
