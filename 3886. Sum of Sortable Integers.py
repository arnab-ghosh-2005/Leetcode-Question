class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        total_sum = 0
        
        # Helper function to check if list A is a cyclic rotation of list B
        def is_cyclic_rotation(A, B):
            if len(A) != len(B):
                return False
            # Convert to string or check subsegments to avoid multiset mismatches
            # Since elements are integers, doing a sublist search:
            double_B = B + B
            # Simple check using sequence search
            for i in range(len(B)):
                if double_B[i:i+len(A)] == A:
                    return True
            return False

        # Try all divisors of n
        for k in range(1, n + 1):
            if n % k == 0:
                possible = True
                for i in range(0, n, k):
                    curr_block = nums[i:i+k]
                    target_block = sorted_nums[i:i+k]
                    
                    if not is_cyclic_rotation(curr_block, target_block):
                        possible = False
                        break
                if possible:
                    total_sum += k
                    
        return total_sum
