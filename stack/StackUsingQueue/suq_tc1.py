from MyStack import MyStack

stack = MyStack()
stack.push(10)
stack.push(20)
stack.push(30)

assert stack.top() == 30
assert stack.pop() == 30
assert stack.top() == 20
assert stack.pop() == 20
assert stack.empty() == False
assert stack.pop() == 10
assert stack.empty() == True
