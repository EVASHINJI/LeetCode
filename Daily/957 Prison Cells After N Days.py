# Url: https://leetcode.com/problems/prison-cells-after-n-days/
# Related Topics:
# HashTable

# Example 1:
# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation: 
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
# Example 2:
# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0]


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def change(state):
            return [int(i > 0 and i < 7 and state[i-1] == state[i+1]) for i in range(8)]
                    
        seen, day = [], 0
        state = tuple(cells)
        while state not in seen and day < N:
            seen.append(state)
            state = change(state)
            day += 1
        if day == N:
            return state
        loop_start = seen.index(state)
        gap = (N - day) % (len(seen) - loop_start)
        return seen[loop_start + gap]