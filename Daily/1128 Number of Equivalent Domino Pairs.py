# Url: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
# Related Topics:
# Array 

# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = {}
        for i, j in dominoes:
            mi, ma = min(i,j), max(i,j)
            cnt[(mi, ma)] = cnt.get((mi,ma), 0) + 1
        ans = 0
        for v in cnt.values():
            ans += v*(v-1)/2
        return int(ans)
        