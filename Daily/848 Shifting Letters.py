# Url: https://leetcode.com/problems/shifting-letters/
# Related Topics:
# String

# Example:
# Input: S = "abc", shifts = [3,5,9]
# Output: "rpl"


class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        shift, new_S = 0, []
        for i in range(len(S) - 1, -1, -1):
            shift = (shift + shifts[i]) % 26
            s = ord(S[i]) + shift
            if s > ord('z'):
                s = s - 26
            new_S.append(chr(s))
        return ''.join(reversed(new_S))