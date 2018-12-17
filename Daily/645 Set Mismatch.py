# Url: https://leetcode.com/problems/set-mismatch/
# Related Topics:
# Math HashTable

# Example:
# Input: nums = [1,2,2,4]
# Output: [2,3]


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        check = [0] * len(nums)
        twice, miss = -1, -1
        for n in nums:
            check[n-1] += 1
        for i in range(len(nums)):
            if check[i] == 2:
                twice = i + 1
            if check[i] == 0:
                miss = i + 1
        return [twice, miss]