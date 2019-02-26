# Url: https://leetcode.com/problems/minimum-index-sum-of-two-lists/
# Related Topics:
# HashTable

# Example:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans, idx_sum = [], len(list1) + len(list2)
        d1 = {name: i for i, name in enumerate(list1)}
        for i, name in enumerate(list2):
            if name in d1:
                print(name)
                if d1[name] + i < idx_sum:
                    ans = [name]
                    idx_sum = d1[name] + i
                elif d1[name] + i == idx_sum:
                    ans.append(name)
        return ans