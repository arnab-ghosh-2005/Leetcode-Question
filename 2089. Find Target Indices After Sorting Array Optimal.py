class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less_than = sum(num < target for num in nums)
        count = nums.count(target)
        return list(range(less_than, less_than + count))
if __name__ == "__main__":
    sol = Solution()
    n1 = [1,2,5,2,3]
    t1 = 2
    res1 = sol.targetIndices(n1,t1)
    print(f"Array = {n1} and target = {t1} ---->  output {res1}")

    n2 = [1,2,5,2,3]
    t2 = 3
    res2 = sol.targetIndices(n2,t2)
    print(f"Array = {n2} and target = {t2} ---->  output {res2}")

    n3 = [1,2,5,2,3]
    t3 = 5
    res3 = sol.targetIndices(n3,t3)
    print(f"Array = {n3} and target = {t3} ---->  output {res3}")
        