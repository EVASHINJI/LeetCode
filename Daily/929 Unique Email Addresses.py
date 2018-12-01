# Url: https://leetcode.com/problems/unique-email-addresses/
# Related Topics:
# String

# Example 1:
# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
 
# Note:
# 1 <= emails[i].length <= 100
# 1 <= emails.length <= 100
# Each emails[i] contains exactly one '@' character.


class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        receive = set()
        for email in emails:
            local, domain = email.split('@')
            plus_idx = local.find('+')
            if plus_idx > 0:
                local = local[:plus_idx]
            local = local.replace('.', '')
            receive.add(local+'@'+domain)
        return len(receive)