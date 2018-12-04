# Url: https://leetcode.com/problems/student-attendance-record-i/
# Related Topics:
# String

# Example:
# Input: "PPALLP"
# Output: True


class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        late = 'LLL' in s
        absent = s.count('A') > 1
        if absent or late:
            return False
        return True