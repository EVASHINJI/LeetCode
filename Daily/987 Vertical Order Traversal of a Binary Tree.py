# Url: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Related Topics:
# HashTable Tree

# Example:
# Input: [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation: 
# The node with value 5 and the node with value 6 have the same position according to the given scheme.
# However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.

from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_X = defaultdict(list)
        def traversal(node, x, y):
            node_X[x].append((y, node.val))
            if node.left: traversal(node.left, x-1, y+1)
            if node.right: traversal(node.right, x+1, y+1)
                
        traversal(root, 0, 0)
        ans = []
        for k in sorted(node_X.keys()):
            ans.append(list(map(lambda x: x[1], sorted(node_X[k]))))
        return ans