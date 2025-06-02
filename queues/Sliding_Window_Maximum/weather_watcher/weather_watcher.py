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

