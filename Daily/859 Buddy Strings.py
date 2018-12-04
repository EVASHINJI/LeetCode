# Url: https://leetcode.com/problems/buddy-strings/
# Related Topics:
# String

# Example:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true


class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            if len(set(A)) < len(A):
                return True
            else:
                return False
        diff = []
        for i, (a, b) in enumerate(zip(A, B)):
            if a != b:
                diff.append(i)
                if len(diff) > 2:
                    return False
        if len(diff) != 2:
            return False
        return A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]