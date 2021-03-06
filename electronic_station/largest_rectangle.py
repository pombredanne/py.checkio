"""
Largest Rectangle in a Histogram

You have a histogram. Try to find size of the biggest rectangle you can build out
of the histogram bars.

Input: List of all rectangles heights in histogram

Output: Area of the biggest rectangle
Precondition:
0 < len(data) < 1000

Reference:
https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
"""

from typing import List


def slow_largest_histogram(histogram: List[int]) -> int:
    """It uses O(n^2)."""
    max_area = 0

    for i, v in enumerate(histogram):
        min_height = v
        for j in range(i, len(histogram)):
            min_height = min(min_height, histogram[j])
            max_area = max(max_area, min_height * ((j - i) + 1))
    return max_area


def largest_histogram(histogram: List[int]) -> int:
    """It uses O(n)."""
    max_area = 0
    stack = []
    top = lambda: stack[-1]
    area = lambda i, length: histogram[stack.pop()] * (
        (i - top() - 1) if stack else length
    )

    for i, v in enumerate(histogram):
        # we are saving indexes in stack that is why we comparing last element in stack
        # with current height to check if last element in stack not bigger then
        # current element
        while stack and v <= histogram[top()]:
            max_area = max(max_area, area(i, i))
        stack.append(i)

    # we went through all elements of histogram
    # check if we have something left in stack
    while stack:
        max_area = max(max_area, area(i, len(histogram)))
    return max_area


if __name__ == "__main__":
    assert slow_largest_histogram([5]) == 5, "one is always the biggest"
    assert slow_largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert slow_largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert slow_largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert slow_largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    assert slow_largest_histogram([3, 1, 6, 3, 5, 0, 8]) == 9, "Google"

    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    assert largest_histogram([3, 1, 6, 3, 5, 0, 8]) == 9, "Google"
    print("Done! Go check it!")
