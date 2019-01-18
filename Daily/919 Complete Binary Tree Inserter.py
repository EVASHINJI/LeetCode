# Url: https://leetcode.com/problems/complete-binary-tree-inserter/
# Related Topics:
# Tree

# Example 1:
# Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
# Output: [null,1,[1,2]]
# Example 2:
# Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
# Output: [null,3,4,[1,2,3,4,5,6,7,8]]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.deque = deque()
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        
    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = TreeNode(v)
        parent = self.deque[0]
        self.deque.append(node)
        if not parent.left:
            parent.left = node
        elif not parent.right:
            parent.right = node
            self.deque.popleft()
        return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()