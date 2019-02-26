# Url: https://leetcode.com/problems/shortest-completing-word/
# Related Topics:
# HashTable

# Example 1:
# Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
# Output: "steps"
# Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
# Note that the answer is not "step", because the letter "s" must occur in the word twice.
# Also note that we ignored case for the purposes of comparing whether a letter exists in the word.
# Example 2:
# Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
# Output: "pest"
# Explanation: There are 3 smallest length words that contains the letters "s".
# We return the one that occurred first.


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_cnt = {}
        for c in licensePlate.lower():
            if c.isalpha():
                license_cnt[c] = license_cnt.get(c, 0) + 1
        ans = '0' * 1001
        for word in words:
            if len(word) < len(ans):
                chars = dict(license_cnt)
                for c in word:
                    if c in chars and chars[c]:
                        chars[c] -= 1
                if not any(chars.values()):
                    ans = word
        return ans