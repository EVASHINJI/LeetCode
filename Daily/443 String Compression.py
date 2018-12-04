# Url: https://leetcode.com/problems/string-compression/
# Related Topics:
# String

# Example:
# Input:
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output:
# Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# in-place


class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        cnt, i = 0, 0
        while i < len(chars):
            prev = chars[i]
            j = i + 1
            while j < len(chars) and chars[j] == prev:
                j += 1
            same = j - i
            if same == 1:
                cnt += 1
                i = i + 1
            else:
                cnt += 1 + len(str(same))
                chars[i+1:j] = str(same)
                i = i + len(str(same)) + 1   
        return cnt
            