class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum > 9 * num:
            return ""
        quotient, remainder = divmod(sum, 9)
        ans = "9" * quotient
        if remainder > 0:
            ans += str(remainder)
        ans += "0" * (num - len(ans))
        return ans

if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    num1 = 2
    sum1 = 3
    result1 = solution.maxSumOfSquares(num1, sum1)
    print(f"Input: num = {num1}, sum = {sum1} -> Output: {result1}")  # Expected: "30"7

    # Test Case 2
    num2 = 2
    sum2 = 17
    result2 = solution.maxSumOfSquares(num2, sum2)
    print(f"Input: num = {num2}, sum = {sum2} -> Output: {result2}")  # Expected: "89"

    
    