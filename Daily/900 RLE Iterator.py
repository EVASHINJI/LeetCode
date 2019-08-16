# Url: https://leetcode.com/problems/rle-iterator/
# Related Topics:
# Array

# Example 1:
# Input: ["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
# Output: [null,8,8,5,-1]
# Explanation: 
# RLEIterator is initialized with RLEIterator([3,8,0,9,2,5]).
# This maps to the sequence [8,8,8,5,5].
# RLEIterator.next is then called 4 times:
# .next(2) exhausts 2 terms of the sequence, returning 8.  The remaining sequence is now [8, 5, 5].
# .next(1) exhausts 1 term of the sequence, returning 8.  The remaining sequence is now [5, 5].
# .next(1) exhausts 1 term of the sequence, returning 5.  The remaining sequence is now [5].
# .next(2) exhausts 2 terms, returning -1.  This is because the first term exhausted was 5,
# but the second term did not exist.  Since the last term exhausted does not exist, we return -1.


class RLEIterator:

    def __init__(self, A: List[int]):
        self.encode = A
        self.counter = 0
        self.pointer = 0
        
    def next(self, n: int) -> int:
        self.counter += n
        while self.pointer < len(self.encode) and self.counter > self.encode[self.pointer]:
            self.counter -= self.encode[self.pointer]
            self.pointer += 2
        if self.pointer < len(self.encode):
            return self.encode[self.pointer+1]
        else:
            return -1
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)