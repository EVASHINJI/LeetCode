# Url: https://leetcode.com/problems/snapshot-array/
# Related Topics:
# Array

# Example 1:
# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation: 
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5


class SnapshotArray:

    def __init__(self, length: int):
        self.snapshot = {i: [[0, 0]] for i in range(length)}
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.snapshot[index][-1][0] == self.snap_id:
            self.snapshot[index][-1][1] = val
        else:
            self.snapshot[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # i, j = 0, len(self.snapshot[index]) 
        # snap_id += 1
        # while i < j:
        #     mid = (i + j) // 2
        #     if self.snapshot[index][mid][0] < snap_id:
        #         i = mid + 1
        #     else:
        #         j = mid
        i = bisect.bisect(self.snapshot[index], [snap_id+1]) 
        return self.snapshot[index][i-1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)