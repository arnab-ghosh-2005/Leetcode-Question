class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        first_digit = 0
        last_digit = 0
        while n > 0:
            n,digit = divmod(n,10)

            if digit > first_digit:
                last_digit = first_digit
                first_digit = digit

            elif digit > last_digit:
                last_digit = digit
            
        return first_digit * last_digit
if __name__ == "__main__":
    sol = Solution()
    n1 = 31
    res1 = sol.maxProduct(n1)
    print(f"for input {n1} output is ---> {res1}")
    n2 = 22
    res2 = sol.maxProduct(n2)
    print(f"for input {n2} output is ---> {res2}")
    n3 = 124
    res3 = sol.maxProduct(n3)
    print(f"for input {n3} output is ---> {res3}")