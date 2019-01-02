# Url: https://leetcode.com/problems/rabbits-in-forest/
# Related Topics:
# Math HashTable

# Example:
# Input: answers = [1, 1, 2]
# Output: 5
# Explanation:
# The two rabbits that answered "1" could both be the same color, say red.
# The rabbit than answered "2" can't be red or the answers would be inconsistent.
# Say the rabbit that answered "2" was blue.
# Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
# The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.


from collections import Counter
class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        cnt = Counter(answers)
        ans = 0
        for key, num in cnt.items():
            ans += ((num - 1) // (key + 1) + 1) * (key + 1)
        return ans