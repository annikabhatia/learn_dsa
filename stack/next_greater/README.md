# 🧠 **Next Greater Element**

---

## 🎯 Objective

Given an array of integers, write a Python function that returns a list where each element is replaced by the **next greater element** on the right side of the array. If there is no greater element, use `-1`.

You’ll use **Python lists** to simulate **stack behavior** and solve this efficiently.

---

## 📥 Input

* A list of integers, e.g., `[4, 5, 2, 10]`

---

## 📤 Output

* A list of integers where each element is replaced with the next greater element, e.g., `[5, 10, 10, -1]`

---

## 🧪 Example

```python
Input: [4, 5, 2, 10]
Output: [5, 10, 10, -1]

Input: [3, 2, 1]
Output: [-1, -1, -1]

Input: [1, 3, 2, 4]
Output: [3, 4, 4, -1]
```

---

## ✅ Task Requirements

1. Write a function named `next_greater_element(arr: List[int]) -> List[int]`
2. Use a **stack (Python list)** to help track potential "next greater" values
3. Traverse the input list **from right to left** (to efficiently use the stack)
4. Do not use built-in functions like `max()` or sort the array
5. You may assume the list has at least one element

---

## 📏 Rules

* ✅ You **must** use Python’s built-in list to simulate a stack (using `.append()` and `.pop()`)
* ❌ Do **not** use `max()` or any sorting functions
* ❌ Do **not** import any external libraries (like NumPy or collections)
* ✅ The function should handle both small and large lists correctly
* ✅ Your code should work for **positive, negative, and zero values**

---

## 💡 Hints

* Use `.append()` and `.pop()` to simulate a stack
* Keep the stack sorted in decreasing order from top to bottom
* At each element, pop from the stack until you find a greater element or the stack is empty
* Start from the **end of the list**, since we’re looking for the next element on the right
* Use a **stack** to keep track of potential greater elements
* Remove elements from the stack if they are less than or equal to the current element
* If the stack is empty, the next greater element is `-1`

---

## 📁 Suggested File

Create a file named `next_greater.py` with:

```python
from typing import List

def next_greater_element(arr: List[int]) -> List[int]:
    # Your code here
    pass

if __name__ == "__main__":
    sample = [4, 5, 2, 10]
    print(next_greater_element(sample))  # Expected: [5, 10, 10, -1]
```

---

## 🙋‍♂️ What to Submit

* Your completed `next_greater.py` file
* Screenshot showing the correct output for at least **three different input arrays**

---
