# Url: https://leetcode.com/problems/spiral-matrix-iii/
# Related Topics:
# Math

# Example:
# Input: R = 1, C = 4, r0 = 0, c0 = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]


class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        def if_in_matrix(r, c):
            if 0 <= r < R and 0 <= c < C:
                return True
            return False
        hori, vert = 1, 1
        dx, dy = 1, 1
        r, c = r0, c0
        cnt = R * C - 1
        ans = [(r0, c0)]
        while cnt:
            for _ in range(hori):
                c = c + dx
                if if_in_matrix(r, c):
                    ans.append([r, c])
                    cnt -= 1
            for _ in range(vert):
                r = r + dy
                if if_in_matrix(r, c):
                    ans.append([r, c])
                    cnt -= 1
            dx, dy = dx*-1, dy*-1
            hori, vert = hori + 1, vert + 1
        return ans
            