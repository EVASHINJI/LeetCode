# Url: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Related Topics:
# HashTable TwoPointers BinarySearch Sort

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        i, j = len(nums1) - 1, len(nums2) - 1
        while i > -1 and j > -1:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i -= 1
                j -= 1
            elif nums1[i] < nums2[j]:
                j -= 1
            else:
                i -= 1
        return ans