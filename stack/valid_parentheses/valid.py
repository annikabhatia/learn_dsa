import sys

input_string = "[(2+4]]"


left_par = ['(', '[', '{']
right_par = [')', ']', '}' ]

matching = {')': '(', ']': '[', '}': '{'}

master_stack = []

for ch in input_string:
    print(ch)
    if (ch in left_par):
        master_stack.append(ch)
    elif (ch in right_par):
        if len(master_stack) == 0:
            print("Stack is empty, String paranthesis do not balance")
            sys.exit() 
        popped_ch = master_stack.pop()
        if (matching[ch] !=  popped_ch):
            print("String parenthesis dont match")
            sys.exit()

if (len(master_stack) > 0):
    print("String parenthesis dont balance")
else:
    print("String parenthesis are valid")
    
