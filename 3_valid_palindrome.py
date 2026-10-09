"""
LeetCode 125: Valid Palindrome
Time Complexity: O(n)
Space Complexity: O(1)
"""


def isPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters case-insensitively
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Example Usage:
if __name__ == "__main__":
    test_str = "A man, a plan, a canal: Panama"
    print(
        f"Is '{test_str}' a palindrome? {isPalindrome(test_str)}"
    )  # Output: True
