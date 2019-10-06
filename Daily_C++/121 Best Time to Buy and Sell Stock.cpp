// Url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Related Topics:
// Array DP

// Example 1:
// Input: [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
//              Not 7-1 = 6, as selling price needs to be larger than buying price.

// Example 2:
// Input: [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transaction is done, i.e. max profit = 0.


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (!prices.size()) return 0;
        int ans = 0, mi = prices[0];
        for (int i = 1; i < prices.size(); i++) {
            int cur = prices[i] - mi;
            if (cur > ans) ans = cur;
            mi = min(prices[i], mi);
        }
        return ans;
    }
};