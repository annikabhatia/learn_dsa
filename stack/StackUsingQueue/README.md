# 📘  **Implement Stack Using Queues**

---

## 🎯 Objective

Your task is to **simulate a stack (Last-In-First-Out)** data structure using only **queues (First-In-First-Out)**. You must implement the four core stack operations using one or more queue(s) and only queue-specific methods.

---

## 📚 Background

In Python:

* A **stack** works on **LIFO** (Last-In-First-Out): The last element added is the first one removed.
* A **queue** works on **FIFO** (First-In-First-Out): The first element added is the first one removed.

Even though these are opposites, we can simulate a stack using queues by carefully moving elements around during operations like `push()` and `pop()`.

Python provides a built-in **queue-like structure** in the `collections` module called `deque`. It allows fast appends and pops from both ends. For this assignment, we will treat `deque` like a **queue**, and only use:

* `append()` → enqueue (add to back)
* `popleft()` → dequeue (remove from front)


---

## ✅ Functional Requirements

Implement a class `MyStack` that supports the following methods:

### `void push(int x)`

* Push element `x` onto the stack.

### `int pop()`

* Removes the element on top of the stack and returns it.

### `int top()`

* Returns the element on the top of the stack without removing it.

### `boolean empty()`

* Returns `true` if the stack is empty, `false` otherwise.

---

## 🔐 Rules

* You are **not allowed to use Python’s built-in list stack methods like `pop()` or `[-1]` directly.**
* You must only use **`collections.deque`** to simulate queue behavior.
* You can use **one or two queues** (as `deque` instances).

---

## 🧪 Example Test Cases

```python
stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.top())    # Output: 3
print(stack.pop())    # Output: 3
print(stack.top())    # Output: 2
print(stack.pop())    # Output: 2
print(stack.empty())  # Output: False
print(stack.pop())    # Output: 1
print(stack.empty())  # Output: True
```

---

## 🧠 Tips for Implementation

There are two possible strategies:

1. **Rearrange the queue on every push** so the newest element is always at the front.
2. **Rearrange the queue on every pop** to retrieve the last added element.

Choose either method. Just make sure the behavior matches a real stack.

---

## 🧑‍💻 Getting Started

Here’s a starting code snippet:

```python
from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x):
        # implement this
        pass

    def pop(self):
        # implement this
        pass

    def top(self):
        # implement this
        pass

    def empty(self):
        # implement this
        pass
```

---

## 📎 Deliverables

* Your completed Python file with class `MyStack`.
* A few test cases in the main section (`if __name__ == '__main__':`) that demonstrate your stack in action.
* Comment your code to explain the logic behind your chosen approach.
