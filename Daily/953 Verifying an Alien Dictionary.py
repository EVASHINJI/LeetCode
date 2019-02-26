# Url: https://leetcode.com/problems/verifying-an-alien-dictionary/
# Related Topics:
# HashTable

# Example 1:
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:
# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {}
        order_index = {c: i for i, c in enumerate(order)}
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if order_index[word1[j]] > order_index[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True
        