# Url: https://leetcode.com/problems/tag-validator/
# Related Topics:
# String Stack

# Example:
# Input: "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
# Output: True


import re
class Solution:
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        code = re.sub('<!\[CDATA\[.*?\]\]>', 'c', code.strip())
        if not code:
            return False
        i, l = 0, len(code)
        start_tag, end_tag = None, None
        stack = []
        while i < l:
            if code[i] == '<':
                end = code.find('>', i+1)
                if end == -1:
                    return False
                tag = code[i+1: end] if code[i+1] != '/' else code[i+2: end]
                if not all('A' <= c <= 'Z' for c in tag) or not (1 <= len(tag) <= 9):
                    return False
                if code[i+1] == '/':
                    if not stack or stack[-1] != tag:
                        return False
                    if end == l - 1:
                        end_tag = tag
                    stack.pop()
                else:
                    if not start_tag:
                        start_tag = tag
                    stack.append(tag)
                i = end
            elif not stack:
                stack.append(code[i])
            i += 1
        if stack or start_tag != end_tag:
            return False
        return True
        