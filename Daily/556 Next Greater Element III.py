# Url: https://leetcode.com/problems/next-greater-element-iii/
# Related Topics:
# String

# Example:
# Input: 12
# Output: 21


class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = list(str(n))
        if len(n) <= 1:
            return -1
        idx = -1
        for i,j in zip(range(len(n)-2, -1, -1), range(len(n)-1, -1, -1)):
            if n[i] < n[j]:
                idx = i
                break
        if idx == -1:
            return -1
        
        nxt_idx = idx + 1
        for i in range(idx + 1, len(n)):
            if n[idx] < n[i] < n[nxt_idx]:
                nxt_idx = i
        n[idx], n[nxt_idx] = n[nxt_idx], n[idx]
        n[idx+1:] = sorted(n[idx+1:])
        ans = int(''.join(n))
        return ans if ans <= ((1<<31)-1) else -1