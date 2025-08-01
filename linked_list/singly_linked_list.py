#Build basic singly linked list.

class Node:
    def __init__(self, data):
        self.data = data  #storing data
        self.next = None  #next part of node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    #insert node to end of the list
    def insert(self, data):
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
            return
        current = self.head
        while current.next:  
            current = current.next
        current.next = new_node

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
