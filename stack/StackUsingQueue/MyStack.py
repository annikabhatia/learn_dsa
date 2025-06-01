from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x):
        self.q2.append(x)
    
        for i in list(self.q1):
            #removes/returns the leftmost element of the deque
            self.q2.append(self.q1.popleft())
    
        #swap 2 queues so q1 can be real stack
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

    def pop(self):
        #Remove element from top of the stack
        return self.q1.popleft()


    def top(self):
        #Returns the element on the top of the stack without removing it.
        return(self.q1[0])

    def empty(self):
        #Returns `true` if the stack is empty, `false` otherwise.
        if len(self.q1) == 0:
            return True
        else:
            return False 
