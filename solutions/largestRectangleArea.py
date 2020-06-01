class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        stk = []
        left_idx = 0
        height = heights[0]
        max_area = 0
        for i, h in enumerate(heights):
            if h > height:
                stk.append((left_idx, height))
                height = h
                left_idx = i
            
            height = min(h, height)
            stk.append((left_idx, height))
            next_height = 0
            if i+1 < len(heights):
                next_height = heights[i+1]
            
            while stk and next_height <= stk[-1][1]:
                left_idx, height = stk.pop()
                height = min(height, h)
                max_area = max(max_area, height*(i-left_idx+1))
        
        return max_area
                
# O(n) time, O(n) space
