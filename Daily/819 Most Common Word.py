# Url: https://leetcode.com/problems/most-common-word/
# Related Topics:
# String

# Example:
# Input: 
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit"]
# Output: "ball"


from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        paragraph_clean = re.sub('[!?\',;.]', ' ', paragraph).lower().split(' ')
        counter = Counter(paragraph_clean)
        for word, _ in counter.most_common():
            if word.isalpha() and word not in banned:
                return word