# Url: https://leetcode.com/problems/vowel-spellchecker/
# Related Topics:
# HashTable String

# Example:
# Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        origin = set(wordlist)
        capitle, vowel = {}, {}
        
        def voweled(word):
            return ''.join([c if c not in 'aeiou' else '*' for c in word])
        
        def solve(q):
            if q in origin:
                return q
            
            q_low = q.lower()
            if q_low in capitle:
                return capitle[q_low]
            
            q_vow = voweled(q_low)
            if q_vow in vowel:
                return vowel[q_vow]
            
            return ""
        
        for w in wordlist:
            w_low = w.lower()
            capitle.setdefault(w_low, w)
            vowel.setdefault(voweled(w_low), w)

        return list(map(solve, queries))