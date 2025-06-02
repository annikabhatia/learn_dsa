class SupportTicketQueue:
    
    #self is a reference to the current instance of the class
    def __init__(self):
        #stores the empty list as an attribute of the object...allows it to be used by other methods!
        self.inbox = []
        self.outbox = []

    # Use `inbox` to store incoming tickets.
    #   When processing or peeking:
    #   If `outbox` is empty, move all items from `inbox` to `outbox` by popping from `inbox` and appending to `outbox`.
    # This simulates queue behavior using only list operations on the end of the list.

    def submit_ticket(self, ticket_description: str):  
        #Adds a new ticket to the end of the queue.
        self.inbox.append(ticket_description)

    def process_ticket(self): 
        #Removes and returns the ticket that was submitted first.
        if len(self.outbox) == 0:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()
          
    def peek_ticket(self):  
        #Returns the ticket at the front of the queue without removing it (aka right-most element)
        if len(self.outbox) == 0:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox[-1]

    def is_empty(self): 
        #Returns `True` if the queue is empty, else `False`
        if len(self.outbox) == 0:
            return True
        else:
            return False

    