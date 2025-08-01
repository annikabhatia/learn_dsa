#Reverse a singly linked list.

def reverse_sll(self):
    prev=None
    current = self.head
    
    while current:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    
    self.head=prev