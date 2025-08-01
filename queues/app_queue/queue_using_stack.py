#Use two stacks to implement a queue.
#LIFO to FIFO

input = [13, 11, 16, 23, 4]

stack = []
stack2 = []

for i in input:
    stack.append(i) 
   
for j in reversed(stack):
    stack2.append(j)

print("Stack in LIFO format: ")
print(stack2)

print("Stack in FIFO format: ")
print(stack)



