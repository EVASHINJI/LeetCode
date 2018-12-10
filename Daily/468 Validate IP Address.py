# Url: https://leetcode.com/problems/validate-ip-address/
# Related Topics:
# String

# Example:
# Input: "172.16.254.1"
# Output: "IPv4"
# Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"
# Output: "IPv6"


class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def is_IPv4(s):
            try:
                s = s.split('.')
                return len(s) == 4 and all([0 <= int(i) < 256 and str(int(i)) == i for i in s])
            except:
                return False
        
        def is_IPv6(s):
            try:
                s = s.split(':')
                return len(s) == 8 and all([len(i) <=4 and '-' not in i and int(i, 16) >= 0 for i in s])
            except:
                return False
            
        if '.' in IP:
            if is_IPv4(IP):
                return "IPv4"
        elif ':' in IP:
            if is_IPv6(IP):
                return "IPv6"
        return "Neither"