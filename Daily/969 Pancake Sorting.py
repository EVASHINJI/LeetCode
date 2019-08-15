# Url: https://leetcode.com/problems/pancake-sorting/
# Related Topics:
# Array Sort 

# Example 1:
# Input: [3,2,4,1]
# Output: [4,2,4,3]
# Explanation: 
# We perform 4 pancake flips, with k values 4, 2, 4, and 3.
# Starting state: A = [3, 2, 4, 1]
# After 1st flip (k=4): A = [1, 4, 2, 3]
# After 2nd flip (k=2): A = [4, 1, 2, 3]
# After 3rd flip (k=4): A = [3, 2, 1, 4]
# After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []
        for x in range(len(A), 0, -1):
            i = A.index(x)
            ans.extend([i+1, x])
            A = A[:i:-1] + A[:i]
        return ans