class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        square = [x*x for x in nums]
        square.sort()
        k = n // 2
        positive_sum = 0
        negative_sum = 0
        for i in range(0,k):
            negative_sum += square[i]
        for i in range(k,len(nums)):
            positive_sum += square[i]
        return positive_sum - negative_sum