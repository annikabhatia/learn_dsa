from weather_watcher import WeatherWatcher

def run_tests():
    print("Running tests for WeatherWatcher...\n")

    # Test Case 1
    temps1 = [30, 32, 35, 33, 31, 36, 38, 34]
    watcher1 = WeatherWatcher(temps1)
    result1 = watcher1.max_in_sliding_window(3)
    print("Test Case 1 - Input:", temps1)
    print("Window Size: 3")
    print("Expected: [35, 35, 35, 36, 38, 38]")
    print("Result:   ", result1)
    print()

    # Test Case 2
    temps2 = [29, 30, 32, 28, 27, 33, 31, 35, 34, 36, 32, 30, 28, 37, 38]
    watcher2 = WeatherWatcher(temps2)
    result2 = watcher2.max_in_sliding_window(5)
    print("Test Case 2 - Input:", temps2)
    print("Window Size: 5")
    print("Expected: [32, 33, 35, 35, 36, 36, 36, 36, 36, 37, 38]")
    print("Result:   ", result2)
    print()

    # Test Case 3 - Edge case: Empty list
    watcher3 = WeatherWatcher([])
    result3 = watcher3.max_in_sliding_window(3)
    print("Test Case 3 - Empty Input")
    print("Expected: []")
    print("Result:   ", result3)
    print()

    # Test Case 4 - Edge case: k = 1 (should return original list)
    temps4 = [28, 29, 30]
    watcher4 = WeatherWatcher(temps4)
    result4 = watcher4.max_in_sliding_window(1)
    print("Test Case 4 - k = 1")
    print("Expected: [28, 29, 30]")
    print("Result:   ", result4)
    print()

if __name__ == "__main__":
    run_tests()
