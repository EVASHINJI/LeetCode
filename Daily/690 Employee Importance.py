# Url: https://leetcode.com/problems/employee-importance/
# Related Topics:
# HashTable DepthFirstSearch BreadthFirstSearch

# Example:
# Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# Output: 11
# Explanation:
# Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.


"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, _id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        employees_dict = {e.id: e for e in employees}
        importance, sub_list = 0, [_id]
        while sub_list:
            new_sub = []
            for s in sub_list:
                e = employees_dict[s]
                new_sub.extend(e.subordinates)
                importance += e.importance
            sub_list = new_sub
        return importance