# Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.
#   A string is considered valid if:
#       Open brackets must be closed by the same type of brackets.
#       Open brackets must be closed in the correct order.
#       Every closing bracket has a corresponding opening bracket of the same type. 

def is_valid(s):
    stack = []
    # creating a dictionary of key-value pairs (ex. key is { and value is } )
    matching = {')': '(', ']': '[', '}': '{'}

    # basically, we want to push the opening brackets, and once we reach the closing bracket, we are checking if it matches
    # the top of the array of chars. if it does, we remove the element that was LAST inserted (stack follows LIFO)
    for char in matching:
        if char in matching.values():
            stack.append(char)
        elif char in matching:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()
    return not stack




