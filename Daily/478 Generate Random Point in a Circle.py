# Url: https://leetcode.com/problems/generate-random-point-in-a-circle/
# Related Topics:
# Math Random RejectionSampling

# Example:
# Input: 
# ["Solution","randPoint","randPoint","randPoint"]
# [[1,0,0],[],[],[]]
# Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]


import random
class Solution:
    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while True:
            dx = random.uniform(-self.radius, self.radius)
            dy = random.uniform(-self.radius, self.radius)
            if dx**2 + dy**2 <= self.radius**2:  
                return [self.x + dx, self.y + dy]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()