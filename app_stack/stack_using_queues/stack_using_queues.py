# Simulate stack operations using queues.
# From LIFO to FIFO; stack behaviors using only queue operations

from collections import deque

queue = deque()

#enqueue
queue.append(10)
queue.append(20)
queue.append(30)


for i in queue:
    print(i)

