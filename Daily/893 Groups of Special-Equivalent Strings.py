# Url: https://leetcode.com/problems/groups-of-special-equivalent-strings/
# Related Topics:
# String

# Example 1:
# Input: ["a","b","c","a","c","c"]
# Output: 3
# Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]
# Example 2:

# Input: ["aa","bb","ab","ba"]
# Output: 4
# Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]
# Example 3:

# Input: ["abc","acb","bac","bca","cab","cba"]
# Output: 3
# Explanation: 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]
# Example 4:

# Input: ["abcd","cdab","adcb","cbad"]
# Output: 1
# Explanation: 1 group ["abcd","cdab","adcb","cbad"]


class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        return len({''.join(sorted(word[::2]) + sorted(word[1::2])) for word in A})