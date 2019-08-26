# Url: https://leetcode.com/problems/minimum-cost-for-tickets/
# Related Topics:
# DP

# Example 1:
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: 
# For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total you spent $11 and covered all the days of your travel.


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N = len(days)
        dp = [float("inf")] * N
        gaps = [1, 7 ,30]
        def run(i):
            if i >= N:
                return 0
            if dp[i] != float("inf"):
                return dp[i]
            
            mi = float('inf')
            j = i
            for c, g in zip(costs, gaps):
                while j < N and days[j] < days[i] + g:
                    j += 1
                mi = min(mi, run(j) + c)
            dp[i] = mi
            return dp[i]
        return run(0)