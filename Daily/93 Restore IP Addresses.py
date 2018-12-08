# Url: https://leetcode.com/problems/restore-ip-addresses/
# Related Topics:
# String BackTracking

# Example:
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        def make(rlt, s, i):
            if len(s) > (5 - i) * 3:
                return
            if i == 5:
                if not s:
                    ans.append(rlt[:-1])
            else:
                for k in range(1, 4):
                    nxt = s[:k]
                    if k > len(s) or not nxt:
                        break
                    if nxt == '0' or int(nxt) < 256 and nxt[0] != '0':
                        make(rlt + nxt + '.', s[k:], i + 1)
                    else:
                        break
        
        if not s:
            return []
        else:
            make("", s, 1)
            return ans
                        