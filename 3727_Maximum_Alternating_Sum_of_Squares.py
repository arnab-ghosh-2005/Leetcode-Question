class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        square = [x*x for x in nums]
        square.sort()
        k = n // 2
        positive_sum = 0
        negative_sum = 0
        for i in range(0, k):
            negative_sum += square[i]
        for i in range(k, len(nums)):
            positive_sum += square[i]
        return positive_sum - negative_sum

# Boilerplate code to execute and test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1 (Odd length)
    test1 = [1, 2, 3]
    result1 = solution.maxAlternatingSum(test1)
    print(f"Input: {test1} -> Output: {result1}")  # Expected: 12
    
    # Test Case 2 (Even length with negatives)
    test2 = [1, -1, 2, -2, 3, -3]
    result2 = solution.maxAlternatingSum(test2)
    print(f"Input: {test2} -> Output: {result2}")  # Expected: 16

