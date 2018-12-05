# Url: https://leetcode.com/problems/reorganize-string/
# Related Topics:
# String Heap Greedy Sort

# Example:
# Input: S = "aab"
# Output: "aba"

# Creative Heap


import itertools
class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        N = len(S)
        A = []
        for cnt, x in sorted([(S.count(x), x) for x in set(S)]):
            if cnt > (N+1)/2:
                return ""
            A.extend(x * cnt)
        
        ans = [None] * N
        ans[::2], ans[1::2] = A[N//2:], A[:N//2]
        return ''.join(ans)


class Solution(object):
    def reorganizeString(self, S):
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            ans.extend([ch1, ch2])
            if nct1 + 1: heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1: heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')