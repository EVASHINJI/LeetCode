# Url: https://leetcode.com/problems/corporate-flight-bookings/
# Related Topics:
# Array Math

# Example 1:
# Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# Output: [10,55,45,25,25]


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i, j, k in bookings:
            ans[i-1] += k
            ans[j] -= k
        for i in range(n):
            ans[i+1] += ans[i]
        return ans[:-1]