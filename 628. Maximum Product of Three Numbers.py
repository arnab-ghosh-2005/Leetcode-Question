class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first_digit = mid_digit = last_digit = float('-inf')
        min1 = min2 = float('inf')
        
        for digit in nums:
            if digit > first_digit:
                last_digit = mid_digit
                mid_digit = first_digit
                first_digit = digit
            elif digit > mid_digit:
                last_digit = mid_digit
                mid_digit = digit
            elif digit > last_digit:
                last_digit = digit
                
            if digit < min1:
                min2 = min1
                min1 = digit
            elif digit < min2:
                min2 = digit
            
        return max(first_digit * mid_digit * last_digit, min1 * min2 * first_digit)

if __name__ == "__main__":
    sol = Solution()
    n1 = [1,2,-3]
    res1 = sol.maximumProduct(n1)
    print(f"for input {n1} output is ---> {res1}")
    n2 = [1,2,3,4]
    res2 = sol.maximumProduct(n2)
    print(f"for input {n2} output is ---> {res2}")
    n3 = [-1,-2,-3]
    res3 = sol.maximumProduct(n3)
    print(f"for input {n3} output is ---> {res3}")