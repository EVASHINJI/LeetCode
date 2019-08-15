# Url: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# Related Topics:
# Array BinarySearch

# Example 1:
# Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# Output: 15
# Explanation: 
# A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid, d, cur = (left + right)//2, 1, 0
            for w in weights:
                if cur + w > mid:
                    cur = 0
                    d += 1
                cur += w
            if d > D:
                left = mid + 1
            else:
                right = mid
        return left