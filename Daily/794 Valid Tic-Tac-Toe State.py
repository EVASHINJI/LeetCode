# Url: https://leetcode.com/problems/valid-tic-tac-toe-state/
# Related Topics:
# Math Recursion

# Example:
# Input: board = ["O  ", "   ", "   "]
# Output: false
# Explanation: The first player always plays "X".


class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        board_s = ''.join(board)
        X_num = board_s.count('X')
        O_num = board_s.count('O')
        if (X_num - O_num) not in [0, 1]:
            return False
        ways = [board_s[0::3], board_s[1::3], board_s[2::3], board_s[0:3], board_s[3:6], board_s[6:], board_s[::4], board_s[2:7:2]]
        winner = set()
        for w in ways:
            if w == 'XXX':
                winner.add('X')
            if w == 'OOO':
                winner.add('O')
        if len(winner) > 1 or ('X' in winner and X_num == O_num) or ('O' in winner and X_num > O_num):
            return False
        return True
