class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = 0
        n = len(nums)
        for i in range(n):
            distinct_set = set()
            for j in range(i,n):
                distinct_set.add(nums[j])
                count = len(distinct_set)
                total_sum += count*count
        return total_sum
if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    nums1 = [1,2,1]
    result1 = solution.sumCounts(nums1)
    print(f"Input: {nums1} -> Output: {result1}")  # Expected: 14   

    # Test case 2
    nums2 = [1,1]
    result2 = solution.sumCounts(nums2)
    print(f"Input: {nums2} -> Output: {result2}")  # Expected: 3