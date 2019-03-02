# Url: https://leetcode.com/problems/array-of-doubled-pairs/
# Related Topics:
# HashTable Array

# Example 1:
# Input: [2,1,2,6]
# Output: false
# Example 2:
# Input: [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].


from collections import Counter
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        cnt = Counter(A)
        for a in sorted(A, key=abs):
            if not cnt[a]:
                continue
            if cnt[2*a]:
                cnt[a] -= 1
                cnt[2*a] -= 1
            else:
                return False
        return True