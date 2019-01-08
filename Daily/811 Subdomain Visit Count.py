# Url: https://leetcode.com/problems/subdomain-visit-count/
# Related Topics:
# HashTable

# Example:
# Input: ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
# Explanation: 
# We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.


from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        stat = defaultdict(lambda: 0)
        for cpdomain in cpdomains:
            cnt, domain = cpdomain.split(' ')
            cnt = int(cnt)
            stat[domain] += cnt
            idx = domain.find('.') + 1
            while idx > 0:
                stat[domain[idx:]] += cnt
                idx = domain.find('.', idx) + 1
        ans = []
        for k, v in stat.items():
            ans.append(str(v) + ' ' + k)
        return ans