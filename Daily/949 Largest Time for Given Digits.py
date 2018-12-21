# Url: https://leetcode.com/problems/largest-time-for-given-digits/
# Related Topics:
# Math

# Example:
# Input: [1,2,3,4]
# Output: "23:41"


from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ans = -1
        for h1, h2, m1, m2 in permutations(A):
            h = h1 * 10 + h2
            m = m1 * 10 + m2
            time = h * 60 + m
            if 0 <= h < 24 and 0 <= m < 60 and time > ans:
                ans = time
        
        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""