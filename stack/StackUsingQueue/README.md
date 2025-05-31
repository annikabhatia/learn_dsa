# 📘 Programming Assignment: **Implement Stack Using Queues**

---

## 🎯 Objective

Your task is to **simulate a stack (Last-In-First-Out)** data structure using only **queues (First-In-First-Out)**. You must implement the four core stack operations using one or more queue(s) and only queue-specific methods.

---

## 📚 Background

A **stack** is a fundamental data structure that follows the **LIFO** principle. A **queue**, on the other hand, follows the **FIFO** principle. Though they seem to serve opposite purposes, it is possible to implement a stack using queues by carefully rearranging elements during each operation.

This assignment will test your understanding of how abstract data structures work, and how to simulate one using another. It also builds problem-solving skills in terms of **algorithm design**, **efficiency**, and **data structure manipulation**.

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

## 🔐 Constraints

* You may only use the **standard operations of a queue**:

  * `enqueue` (add to back)
  * `dequeue` (remove from front)
  * `peek` or `front` (view front)
  * `isEmpty` (check if empty)
* You may use:

  * One queue (for extra challenge), or
  * Two queues
* You may use any programming language (Python preferred for submission).
* Do **not use built-in stack or list methods like `.pop()` or `.append()` directly to simulate stack behavior.**

---

## 🧪 Example Test Cases

### Test Case 1:

```python
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
```

### Test Case 2:

```python
stack = MyStack()
stack.push(100)
assert stack.top() == 100
stack.push(200)
assert stack.pop() == 200
stack.push(300)
assert stack.top() == 300
```

---

## 🧠 Suggested Implementation Approaches

You can choose between:

1. **Costly Push, Cheap Pop:** Rearrange the queue during `push()`
2. **Cheap Push, Costly Pop:** Rearrange the queue during `pop()`

Clearly comment your approach in the code.
  * Explains which approach you used
  * Time & space complexity for each operation
  * Any challenges or trade-offs you considered

---
