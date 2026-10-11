class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        total_sum = 0
        n = len(arr)
        
        for i in range(n):
            left_choices = i + 1
            right_choices = n - i
            
            total_subarrays = left_choices * right_choices
            
            odd_subarrays = (total_subarrays + 1) // 2
            
            total_sum += odd_subarrays * arr[i]
            
        return total_sum