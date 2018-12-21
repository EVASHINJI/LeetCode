# Url: https://leetcode.com/problems/range-addition-ii/
# Related Topics:
# Math

# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14


import math
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        sums = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sums += i
                if i * i != num:
                    sums += num / i
                    if sums > num:
                        return False
        return sums == num