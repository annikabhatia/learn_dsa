from typing import List

def next_greater_element(arr: List[int]) -> List[int]:
    stack = []
    for i in arr:
        #condition should be that we need to reach 2nd element some how...so maybe just ignore first element?
        while arr
            stack.append(i)
        if i - len(arr) == 0:
            stack.append(-1)
    return stack



if __name__ == "__main__":
    sample = [4, 5, 2, 10]
    print(next_greater_element(sample))  # Expected: [5, 10, 10, -1]
