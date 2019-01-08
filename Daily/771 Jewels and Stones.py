# Url: https://leetcode.com/problems/jewels-and-stones/
# Related Topics:
# HashTable

# Example:
# Input: J = "aA", S = "aAAbbbb"
# Output: 3


class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        J_set = set(J)
        cnt = 0
        for s in S:
            if s in J_set:
                cnt += 1
        return cnt