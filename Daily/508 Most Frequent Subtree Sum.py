# Url: https://leetcode.com/problems/most-frequent-subtree-sum/
# Related Topics:
# Tree HashTable

# Examples 1
# Input:
#   5
#  /  \
# 2   -3
# return [2, -3, 4], since all the values happen only once, return all of them in any order.
# Examples 2
# Input:
#   5
#  /  \
# 2   -5
# return [2], since 2 happens twice, however -5 only occur once.


from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def treeSum(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            value = root.val
            left_vals = treeSum(root.left)
            right_vals = treeSum(root.right)
            if left_vals: value += left_vals[0]
            if right_vals: value += right_vals[0]
            return [value] + left_vals + right_vals
        
        dic = defaultdict(lambda: 0)
        for v in treeSum(root):
            dic[v] += 1
        frequent = 1
        ans = []
        for k, v in dic.items():
            if v == frequent:
                ans.append(k)
            elif v > frequent:
                ans = [k]
                frequent = v
        return ans