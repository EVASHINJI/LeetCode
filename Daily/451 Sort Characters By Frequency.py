# Url: https://leetcode.com/problems/sort-characters-by-frequency/
# Related Topics:
# HashTable Heap

# Example:
# Input: "tree"
# Output: "eert"
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.


from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        ans = ''
        for c, times in cnt.most_common():
            ans += c * times
        return ans