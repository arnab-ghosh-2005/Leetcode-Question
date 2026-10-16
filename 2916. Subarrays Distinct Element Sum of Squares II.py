class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        n = len(nums)
        MOD = 10**9 + 7
        for i in range(n):
            distnict_set = set()
            for j in range(i,n):
                distnict_set.add(nums[j])
                count = len(distnict_set)
                total_sum = (total_sum + count * count) % MOD
        return total_sum
if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    nums1 = nums = [1,2,1]
    result1 = solution.sumCounts(nums1)
    print(f"Input: {nums1} -> outputs: {result1}")  # Expected: 15

    # Test Case 2
    nums2 = [2,2]
    result2 = solution.sumCounts(nums2)
    print(f"Inputs : {nums2} -> outputs : {result2}")  # Expected: 3