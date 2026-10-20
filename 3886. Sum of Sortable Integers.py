class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = 0
        
        for k in range(1, n + 1):
            if n % k != 0:
                continue
                
            possible = True
            prev_max = -1
            
            for i in range(0, n, k):
                # Track drops, min, and max for the current block
                drops = 0
                b_min = nums[i]
                b_max = nums[i]
                
                for j in range(k):
                    curr_val = nums[i + j]
                    next_val = nums[i + (j + 1) % k]
                    
                    if curr_val > next_val:
                        drops += 1
                        
                    if curr_val < b_min:
                        b_min = curr_val
                    if curr_val > b_max:
                        b_max = curr_val
                
                # Condition 1: A block can have at most 1 circular drop
                if drops > 1:
                    possible = False
                    break
                    
                # Condition 2: Next block elements must be >= previous block elements
                if prev_max > b_min:
                    possible = False
                    break
                    
                prev_max = b_max
                
            if possible:
                total_sum += k
                
        return total_sum
