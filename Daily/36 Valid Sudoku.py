# Url: https://leetcode.com/problems/valid-sudoku/
# Related Topics:
# HashTable

# Example 1:
# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# Example 2:
# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being 
#     modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(l):
            seen = set()
            for c in l:
                if c in seen:
                    return False
                else:
                    seen.add(c)
            return True
        
        row_cache = defaultdict(list)
        col_cache = defaultdict(list)
        sub_cache = defaultdict(list)
    
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if not c.isdigit():
                    continue
                row_cache[i].append(c)
                col_cache[j].append(c)
                sub_cache[(i//3, j//3)].append(c)
                
        for cache in [row_cache, col_cache, sub_cache]:
            for v in cache.values():
                if not is_valid(v):
                    return False
        return True