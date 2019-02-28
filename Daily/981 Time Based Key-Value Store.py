# Url: https://leetcode.com/problems/time-based-key-value-store/
# Related Topics:
# HashTable BinarySearch

# Example 1:
# Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# Output: [null,null,"bar","bar",null,"bar2","bar2"]
# Explanation:   
# TimeMap kv;   
# kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1   
# kv.get("foo", 1);  // output "bar"   
# kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"   
# kv.set("foo", "bar2", 4);   
# kv.get("foo", 4); // output "bar2"   
# kv.get("foo", 5); //output "bar2"   
# Example 2:
# Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
# Output: [null,null,null,"","high","high","low","low"]


from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.M = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.M[key]
        if not values:
            return ""
        i = bisect.bisect(values, (timestamp, chr(127)))
        return values[i-1][1] if i else ""
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)