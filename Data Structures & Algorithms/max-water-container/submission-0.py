class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        result = 0

        while p1 < p2:
            height = min(heights[p1], heights[p2])
            width = p2 - p1

            area = width * height

            if area > result:
                result = area
            
            if heights[p1] > heights[p2]:
                p2 -= 1
            else:
                p1 += 1
    
        return result