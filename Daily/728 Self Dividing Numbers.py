# Url: https://leetcode.com/problems/self-dividing-numbers/
# Related Topics:
# Math

# Example:
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing(num):
            for c in str(num):
                if c == '0' or num % int(c):
                    return False
            return True
        
        ans = []
        for i in range(left, right + 1):
            if is_self_dividing(i):
                ans.append(i)
        return ans