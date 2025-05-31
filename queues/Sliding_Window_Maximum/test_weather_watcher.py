from temperature_analyzer import TemperatureAnalyzer

def run_tests():
    print("Running tests for TemperatureAnalyzer...\n")

    # Test Case 1
    temps1 = [30, 32, 35, 33, 31, 36, 38, 34]
    analyzer1 = TemperatureAnalyzer(temps1)
    result1 = analyzer1.max_in_sliding_window(3)
    print("Test Case 1 - Input:", temps1)
    print("Window Size: 3")
    print("Expected: [35, 35, 35, 36, 38, 38]")
    print("Result:   ", result1)
    print()

    # Test Case 2
    temps2 = [29, 30, 32, 28, 27, 33, 31, 35, 34, 36, 32, 30, 28, 37, 38]
    analyzer2 = TemperatureAnalyzer(temps2)
    result2 = analyzer2.max_in_sliding_window(5)
    print("Test Case 2 - Input:", temps2)
    print("Window Size: 5")
    print("Expected: [32, 33, 35, 35, 36, 36, 36, 36, 36, 37, 38]")
    print("Result:   ", result2)
    print()

    # Test Case 3 - Edge case: Empty list
    analyzer3 = TemperatureAnalyzer([])
    result3 = analyzer3.max_in_sliding_window(3)
    print("Test Case 3 - Empty Input")
    print("Expected: []")
    print("Result:   ", result3)
    print()

    # Test Case 4 - Edge case: k = 1 (should return original list)
    temps4 = [28, 29, 30]
    analyzer4 = TemperatureAnalyzer(temps4)
    result4 = analyzer4.max_in_sliding_window(1)
    print("Test Case 4 - k = 1")
    print("Expected: [28, 29, 30]")
    print("Result:   ", result4)
    print()

if __name__ == "__main__":
    run_tests()
