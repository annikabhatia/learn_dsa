
# 🧾 Support Ticket Queue Using Python Lists

## 📌 Assignment Title:
**HelpDesk Hero: Build a Support Ticket Queue Using Python Lists**

---

## 🎯 Objective

Simulate a real-world **Help Desk support system**, where support tickets are processed **in the order they arrive** — just like a queue. However, you must build this queue using only **two Python lists** and **basic list operations** (`append()` and `pop()`).

This assignment teaches how to simulate **FIFO (First-In-First-Out)** behavior using only list operations, while building confidence with **Python classes and methods**.

---

## 🧑‍💻 Scenario

You're designing the ticket-handling system for a company's help desk. Customers submit support tickets describing their issues. These tickets should be handled **in the order they were submitted**.

But here's the challenge: you're only allowed to use **two Python lists**. You can only work with the **end of each list** using:

- `append()` → to add an item to the end
- `pop()` → to remove an item from the end

---

## 🧠 Concepts Practiced

- Queue behavior using list operations
- Python class design
- Simulating data structures
- Logical thinking under constraints

---

## 📋 Problem Statement

Create a Python class named `SupportTicketQueue` using **two lists**: `inbox` and `outbox`.

### Implement the following methods:

- `submit_ticket(ticket_description: str)`  
  ➤ Adds a new ticket to the end of the queue.

- `process_ticket()`  
  ➤ Removes and returns the ticket that was submitted first.

- `peek_ticket()`  
  ➤ Returns the ticket at the front of the queue without removing it.

- `is_empty()`  
  ➤ Returns `True` if the queue is empty, else `False`.

---

## 🧪 Example Usage

```python
queue = SupportTicketQueue()

queue.submit_ticket("Cannot log in to account.")
queue.submit_ticket("Website is down.")
queue.submit_ticket("Reset password issue.")

print(queue.peek_ticket())    # Output: Cannot log in to account.
print(queue.process_ticket()) # Output: Cannot log in to account.
print(queue.process_ticket()) # Output: Website is down.
print(queue.is_empty())       # Output: False
print(queue.process_ticket()) # Output: Reset password issue.
print(queue.is_empty())       # Output: True
```

---

## 💡 Implementation Hint

* Use `inbox` to store incoming tickets.
* When processing or peeking:

  * If `outbox` is empty, move all items from `inbox` to `outbox` by popping from `inbox` and appending to `outbox`.
* This simulates queue behavior using only list operations on the end of the list.

---

## 🔐 Rules

* Use **only `append()` and `pop()`** on lists.
* Do **not** use:

  * `insert()`
  * `pop(0)`
  * `collections.deque`
  * `queue.Queue` or any other built-in queue data structures
* Handle the empty queue gracefully. For example, return `"No tickets to process."` when appropriate.

---

## 🌟 Bonus Challenge

Add a method:

* `ticket_count()`
  ➤ Returns the total number of tickets in the queue, whether in `inbox`, `outbox`, or both.

---

## 📤 Submission Instructions

Submit a Python file named `support_ticket_queue.py` that includes:

* The `SupportTicketQueue` class
* A `main()` function with test cases demonstrating all methods

---

## 🏁 Learning Outcome

You’ll learn how to:

* Simulate a queue using only Python lists
* Build a class-based solution
* Think logically under constraints
* Apply these ideas to a real-world inspired scenario

