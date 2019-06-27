# Url: https://leetcode.com/problems/two-city-scheduling/
# Related Topics:
# Greedy

# Example 1:
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        l = len(costs)
        return sum([x[0] for x in costs[:l//2]]) + sum([x[1] for x in costs[l//2:]])