"""
LeetCode 11: Container With Most Water
Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height

        max_water = max(max_water, current_area)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# Example Usage:
if __name__ == "__main__":
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Max Water Area: {maxArea(heights)}")  # Output: 49
