# Url: https://leetcode.com/problems/fibonacci-number/
# Related Topics:
# Array

# Example 1:
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        f1, f2 = 0, 1
        for _ in range(N - 1):
            f1, f2 = f2, f1 + f2
        return f2