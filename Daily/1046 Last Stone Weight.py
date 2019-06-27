# Url: https://leetcode.com/problems/last-stone-weight/
# Related Topics:
# Greedy Heap

# Example 1:
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-s for s in stones]
        heapq.heapify(q)
        while q:
            s1 = heapq.heappop(q)
            if not q:
                return -s1
            s2 = heapq.heappop(q)
            if s1 != s2:
                heapq.heappush(q, -abs(s1-s2))
        return 0