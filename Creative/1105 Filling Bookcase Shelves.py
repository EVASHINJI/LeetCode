# Url: https://leetcode.com/problems/filling-bookcase-shelves/
# Related Topics:
# DP

# Example:

# Creative
# init by the worst result then merge the posible situation to calculate the min


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        l = len(books)
        dp = [0] * (l + 1)
        for i in range(1, l+1):
            w, h = books[i-1]
            dp[i] = dp[i-1] + h
            j = i - 2
            while j >= 0 and w + books[j][0] <= shelf_width:
                h = max(h, books[j][1])
                w += books[j][0]
                dp[i] = min(dp[i], dp[j] + h)
                j -= 1
        return dp[-1]
            