# Design a stack that returns the minimum element in O(1) time.

input_array = [18, 19, 27, 15, 21]

stack = []
adj_stack = []
min_value = input_array[0]

for i in input_array:
    stack.append(i)
    if not adj_stack or i < min_value:
        adj_stack.append(i)
        min_value = i
    else:
        adj_stack.append(min_value)
    for i,j in zip(reversed(stack),reversed(adj_stack)):
        print(i,j) 
    print("------------------")
    
        
    


