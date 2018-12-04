# Url: https://leetcode.com/problems/count-and-say/
# Related Topics:
# String

# Example:
# Input: 4
# Output: "1211"


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        say = '1'
        for i in range(1, n):
            g = [(len(list(grp)), k) for k, grp in itertools.groupby(say)]
            say = ""
            for cnt, k in g:
                say += "%d%s" % (cnt, k)
        return say