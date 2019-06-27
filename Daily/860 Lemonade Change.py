# Url: https://leetcode.com/problems/lemonade-change/
# Related Topics:
# Greedy

# Example 1:
# Input: [5,5,5,10,20]
# Output: true
# Explanation: 
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.
# Example 2:
# Input: [5,5,10]
# Output: true


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5, c10 = 0, 0
        for b in bills:
            if b == 5:
                c5 += 1
            elif b == 10 and c5:
                c5 -= 1
                c10 += 1
            elif b == 20:
                if c5 and c10:
                    c5 -= 1
                    c10 -= 1
                    continue
                if c5 >= 3:
                    c5 -= 3
                    continue
                return False
            else:
                return False
        return True