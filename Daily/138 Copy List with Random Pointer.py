# Url: https://leetcode.com/problems/copy-list-with-random-pointer/
# Related Topics:
# HashTable LinkedList

# Example:
# Input:
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# Explanation:
# Node 1's value is 1, both of its next and random pointer points to Node 2.
# Node 2's value is 2, its next pointer points to null and its random pointer points to itself.


"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        copy_h = node = Node(head.val, None, None)
        new2random = {node: head.random}
        old2new = {head: node}
        
        while head.next:
            node.next = Node(head.next.val, None, None)
            head, node = head.next, node.next
            new2random[node] = head.random
            old2new[head] = node
        for new, rand in new2random.items():
            if rand: new.random = old2new[rand]
        return copy_h