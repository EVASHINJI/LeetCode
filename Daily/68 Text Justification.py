# Url: https://leetcode.com/problems/text-justification/
# Related Topics:
# String

# Example:
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def justify(line, width):
            slot = len(line) - 1
            space = maxWidth - width
            if not slot:
                return line[0] + ' ' * space
            d, m = space // slot + 1, space % slot
            line_s = ""
            for word in line[:-1]:
                line_s += word + ' ' * d
                if m:
                    line_s += ' '
                    m -= 1
            line_s += line[-1]
            return line_s
                
        width, line = 0, []
        ans = []
        for word in words:
            space = 1 if width else 0
            if width + len(word) + space == maxWidth:
                line.append(word)
                ans.append(' '.join(line))
                width, line = 0, []
            elif width + len(word) + space > maxWidth:
                ans.append(justify(line, width))
                width = len(word)
                line = [word]
            else:
                line.append(word)
                width += len(word) + space
        if line:
            ans.append(' '.join(line) + ' ' * (maxWidth - width))
        return ans