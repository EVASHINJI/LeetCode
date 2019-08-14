# Url: https://leetcode.com/problems/relative-sort-array/
# Related Topics:
# Array Sort

# Example 1:
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        idx_map = {x:i for i, x in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (idx_map.get(x, len(arr2)), x))