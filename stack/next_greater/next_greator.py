from typing import List

def next_greater_element(arr: List[int]) -> List[int]:
    stack = []
    result = []
    greatest_element = arr[len(arr) - 1]
    #Start from the end of the list, since we’re looking for the next element on the right
    for i in reversed(arr):
        #Keep the stack sorted in decreasing order from top to bottom
        if stack and i > i - 1:
            stack.append(i)
            greatest_element = i
        else:
            stack.append(greatest_element)
        #if the stack is empty, the next greater element is `-1`
        if not stack:
            result.append(-1)

    return result



if __name__ == "__main__":
    sample = [4, 5, 2, 10]
    print(next_greater_element(sample))  # Expected: [5, 10, 10, -1]
