from collections import deque

class WeatherWatcher:
    def __init__(self, data: list[int]):
        """
        Initialize the WeatherWatcher with a list of temperature readings.

        :param data: List of integer temperature values
        """
        self.data = data

    def max_in_sliding_window(self, k: int) -> list[int]:
        """
        Returns a list of maximum temperatures for each sliding window of size k.
        This method should be implemented using a deque for O(n) efficiency.

        :param k: Size of the sliding window
        :return: List of maximums for each window
        """
        # TODO: Implement this method using collections.deque
        # 1. Create an empty deque to store indices
        # 2. Loop through the temperature data
        # 3. Maintain the deque such that it always contains indices of potential max elements
        # 4. Append the maximum of each valid window to the result list
        # 5. Return the result list

        pass  # <-- Remove this once implementation is complete
