# Url: https://leetcode.com/problems/top-k-frequent-elements/
# Related Topics:
# HashTable Heap

# Example:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]


import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        return heapq.nlargest(k, cnt.keys(), key=cnt.get)