# Url: https://leetcode.com/problems/daily-temperatures/
# Related Topics:
# HashTable Stack

# Example 1:
# Input: T = [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1, 1, 4, 2, 1, 1, 0, 0]

# Creative
# use stack to record the larger temperature in scopes have met
# use the ans itself to find the next larger temperature


# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         stack = []
#         ans = [0] * len(T)
#         for i in range(len(T) - 1, -1, -1):
#             while stack and T[i] >= T[stack[-1]]:
#                 stack.pop()
#             if stack:
#                 ans[i] = stack[-1] - i
#             stack.append(i)
#         return ans

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        for i in range(len(T) - 2, -1, -1):
            nxt = i + 1
            while T[i] >= T[nxt]:
                if ans[nxt] == 0:
                    break
                nxt += ans[nxt]
            else:
                ans[i] = nxt - i
        return ans