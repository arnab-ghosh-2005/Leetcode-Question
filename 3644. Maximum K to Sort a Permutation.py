class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        max_k = -1
        
        for i, val in enumerate(nums):
            if val != i:
                if max_k == -1:
                    max_k = val
                else:
                    max_k &= val
                    
        return max_k if max_k != -1 else 0