class Solution(object):
    def sumOfDigits(self,nums):
        total = 0
        while nums > 0:
            digit = nums % 10
            total += digit
            nums = nums // 10
        return total
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        n = len(nums)
        for i in range(n):
            res = self.sumOfDigits(nums[i])
            if res == i:
                temp.append(i)
        if len(temp) == 0:
            return -1
        else:
            return min(temp)


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1 
    nums1 = [1,3,2]
    result1 = sol.smallestIndex(nums1)
    print(f"Inputs : {nums1} - > output : {result1}") # Expected 2

    # Test Case 2
    nums2 = [1,10,11]
    result2 = sol.smallestIndex(nums2)
    print(f"Inputs : {nums2} - > output : {result2}")  # Expected 1

    # Test Case 3
    nums3 = [1,2,3]
    result3 = sol.smallestIndex(nums3)
    print(f"Inputs : {nums3} - > output : {result3}") # Expected -1