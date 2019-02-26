# Url: https://leetcode.com/problems/design-hashset/
# Related Topics:
# HashTable Design

# Example:
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);         
# hashSet.add(2);         
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);          
# hashSet.contains(2);    // returns true
# hashSet.remove(2);          
# hashSet.contains(2);    // returns false (already removed)


class ListNode:
    
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.lists = [None] * self.size
        
    def add(self, key: int) -> None:
        idx = key % self.size
        if not self.lists[idx]:
            self.lists[idx] = ListNode(key)
        else:
            cur = self.lists[idx]
            while cur:
                if cur.key == key:
                    return
                if not cur.next: break
                cur = cur.next
            cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        idx = key % self.size
        cur = self.lists[idx]
        if not cur:
            return
        if cur.key == key:
            self.lists[idx] = cur.next
            return
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        idx = key % self.size
        cur = self.lists[idx]
        while cur:
            if cur.key == key:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)