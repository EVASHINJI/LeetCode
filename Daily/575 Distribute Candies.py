# Url: https://leetcode.com/problems/distribute-candies/
# Related Topics:
# HashTable

# Example:
# Input: candies = [1,1,2,2,3,3]
# Output: 3
# Explanation:
# There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
# Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
# The sister has three different kinds of candies. 

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(candies)//2, len(set(candies)))