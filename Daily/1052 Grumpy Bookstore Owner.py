# Url: https://leetcode.com/problems/grumpy-bookstore-owner/
# Related Topics:
# Array SlidingWindow

# Example 1:
# Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
# Output: 16
# Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
# The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        sum_s = [0]
        ma, ma_i, ma_j = 0, 0, 0
        i = 1
        for c, g in zip(customers, grumpy):      
            sum_s.append(c*g + sum_s[-1])
            if i >= X and sum_s[i] - sum_s[i-X] > ma:
                ma, ma_i, ma_j = sum_s[i] - sum_s[i-X], i-X, i
            i += 1            
        
        ans = 0
        for idx, (c, g) in enumerate(zip(customers, grumpy)):
            if ma_i <= idx < ma_j:
                g = 0
            if not g:
                ans += c
        return ans