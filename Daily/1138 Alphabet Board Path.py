# Url: https://leetcode.com/problems/alphabet-board-path/
# Related Topics:
# String HashTable

# Example 1:
# Input: target = "leet"
# Output: "DDR!UURRR!!DDD!"

# Example 2:
# Input: target = "code"
# Output: "RR!DDRR!UUL!R!"


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        def get_path(delta, pos, neg):
            if delta >= 0:
                return pos * delta
            else:
                return neg * abs(delta)
            
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        pos = {}
        for i, row in enumerate(board):
            for j, c in enumerate(board[i]):
                pos[c] = (i, j)
        
        cur = 'a'
        ans = ''
        for c in target:
            dx, dy = pos[c][0] - pos[cur][0], pos[c][1] - pos[cur][1]
            if c == 'z':
                ans += get_path(dy, 'R', 'L')
                ans += get_path(dx, 'D', 'U')
            else:
                ans += get_path(dx, 'D', 'U')
                ans += get_path(dy, 'R', 'L')
            ans += '!'
            cur = c
        return ans