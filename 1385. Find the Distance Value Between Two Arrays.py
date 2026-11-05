import bisect

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            idx = bisect.bisect_left(arr2, x - d)
            
            if idx < len(arr2) and arr2[idx] <= x + d:
                continue
            
            distance_value += 1
            
        return distance_value
