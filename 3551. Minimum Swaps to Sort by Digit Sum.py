class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        
        def get_digit_sum(num: int) -> int:
            s = 0
            while num:
                s += num % 10
                num //= 10
            return s
            
        sorted_nums = sorted(nums, key=lambda x: (get_digit_sum(x), x))
        target_pos = {num: i for i, num in enumerate(sorted_nums)}
        
        swaps = 0
        i = 0
        
        arr = list(nums)
        while i < n:
            correct_idx = target_pos[arr[i]]
            
            if correct_idx != i:
                arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
                swaps += 1
            else:
                i += 1
                
        return swaps
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1 = [10, 20, 30]
    result1 = sol.minSwaps(nums1)
    print(f"Input: {nums1} -> Output: {result1}")  # Expected: 0

    # Test Case 2
    nums2 = [21, 12, 3]
    result2 = sol.minSwaps(nums2)
    print(f"Input: {nums2} -> Output: {result2}")  # Expected: 1

    # Test Case 3
    nums3 = [5, 15, 25, 35]
    result3 = sol.minSwaps(nums3)
    print(f"Input: {nums3} -> Output: {result3}")  # Expected: 0