# Url: https://leetcode.com/problems/reveal-cards-in-increasing-order/
# Related Topics:
# Array 

# Example 1:
# Input: [17,13,11,2,3,5,7]
# Output: [2,13,3,11,5,17,7]
# Explanation: 
# We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
# After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
# We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
# We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
# We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
# We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
# We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
# We reveal 13, and move 17 to the bottom.  The deck is now [17].
# We reveal 17.
# Since all the cards revealed are in increasing order, the answer is correct.


from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        idx = deque(range((N)))
        ans = [0] * N
        
        for card in sorted(deck):
            ans[idx.popleft()] = card
            if idx:
                idx.append(idx.popleft())
                
        return ans