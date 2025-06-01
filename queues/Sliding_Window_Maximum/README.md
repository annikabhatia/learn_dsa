# 🌬️ Weather Watcher: Sliding Window Maximum Using Deque

## 📌 Assignment Title:
**"Weather Watcher: Find Maximum Temperatures in Sliding Windows Using Deques"**

---

## 🎯 Objective

You’ll analyze hourly temperature data using a **sliding window algorithm** and determine the **maximum temperature in each window** of fixed size `k`.

This assignment teaches you:
- How to use `collections.deque` efficiently
- How to apply the **sliding window technique** to real-world problems
- How to build modular Python programs and test them in **Visual Studio Code**

---

## 🧑‍💻 Scenario

You're building a module for a weather app. The system receives a list of hourly temperature readings and must return the **maximum temperature in each window** of size `k` (e.g., every 3-hour, 6-hour segment, etc.). You must build this efficiently — no brute force.

---

## 🧠 Concepts Practiced

- Sliding window technique
- Efficient deque operations
- Class and function design
- Input validation and edge case handling
- Using VS Code for Python development

---

## 📋 Problem Statement

Write a function:

```python
def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    ...
```

You may also optionally wrap this in a class.

---

## 🔄 Input Parameters:

* `nums`: A list of integers (temperatures)
* `k`: An integer window size (1 ≤ k ≤ len(nums))

---

## ✅ Expected Output:

A list of maximum values for each sliding window of size `k`.

---

## 🧪 Example 1

```python
nums = [30, 32, 35, 33, 31, 36, 38, 34]
k = 3
print(sliding_window_maximum(nums, k))
# Output: [35, 35, 35, 36, 38, 38]
```

---

## 🧪 Example 2 – Longer Input

```python
nums = [29, 30, 32, 28, 27, 33, 31, 35, 34, 36, 32, 30, 28, 37, 38]
k = 5
print(sliding_window_maximum(nums, k))
# Output: [32, 33, 35, 35, 36, 36, 36, 36, 36, 37, 38]
```

Explanation:

* Each result is the max of a 5-number window (first: \[29, 30, 32, 28, 27] → 32, next: \[30, 32, 28, 27, 33] → 33, and so on)

---

## 💡 Implementation Hints

* Use `collections.deque` to store **indices** of useful elements.
* At each step:

  * Remove indices from the front of the deque if they're outside the window.
  * Remove from the back of the deque while the current value is greater than the last in deque.
  * Append the current index.
  * The front of the deque always holds the index of the current window’s maximum.

---

## 🔐 Rules

* Use **only** `collections.deque` for optimization.
* Your solution should run in **O(n)** time (linear).
* Handle invalid inputs (e.g., empty list, `k = 0`, `k > len(nums)`) with appropriate error messages.

---

## 🌟 Bonus Challenge

Wrap your logic in a class:

```python
class TemperatureAnalyzer:
    def __init__(self, data: list[int]):
        ...

    def max_in_sliding_window(self, k: int) -> list[int]:
        ...
```

---

## 🛠️ Project Setup Instructions (VS Code)

Follow these steps to set up and run your program:

### 1. 📁 Create Your Project Folder

Create a new folder, e.g., `weather_watcher`.

### 2. 📄 Inside It, Create a File Named:

```
weather_watcher.py
```

### 3. 🧠 Starter Template (Optional)

Paste this into your file:

```python
from collections import deque

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if not nums or k == 0:
        return []

    max_values = []
    dq = deque()

    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            max_values.append(nums[dq[0]])

    return max_values

def main():
    temps = [29, 30, 32, 28, 27, 33, 31, 35, 34, 36, 32, 30, 28, 37, 38]
    k = 5
    result = sliding_window_maximum(temps, k)
    print(f"Max temperatures for every {k}-hour window: {result}")

if __name__ == "__main__":
    main()
```

### 4. ▶️ Run It in VS Code

* Open the folder in VS Code
* Open `weather_watcher.py`
* Press `Ctrl+Shift+P`, select **Run Python File**, or right-click and choose **"Run Python File in Terminal"**

You should see output like:

```
Max temperatures for every 5-hour window: [32, 33, 35, 35, 36, 36, 36, 36, 36, 37, 38]
```

---

## 📤 Submission Instructions

* Submit your `weather_watcher.py` file.
* Ensure it has:

  * `sliding_window_maximum()` function
  * Optional class `TemperatureAnalyzer`
  * A `main()` function with example use cases

---

## 🏁 Learning Outcomes

After completing this assignment, you'll:

* Understand and implement the sliding window maximum pattern
* Use `deque` to optimize performance
* Write modular, efficient Python code
* Develop and run Python projects confidently in **VS Code**

---

