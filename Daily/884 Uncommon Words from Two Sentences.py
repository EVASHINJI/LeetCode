# Url: https://leetcode.com/problems/uncommon-words-from-two-sentences/
# Related Topics:
# HashTable

# Example:
# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
# Input: A = "apple apple", B = "banana"
# Output: ["banana"]

import re
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """ 
        return [k for k, v in Counter((A+' '+B).split(' ')).items() if v == 1]