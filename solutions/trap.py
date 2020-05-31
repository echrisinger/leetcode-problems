class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        max_h, max_i = height[0], 0
        for i, h in enumerate(height):
            if max_h < h:
                max_h = h
                max_i = i
        
        left_stk = [(max_i, max_h)]
        left_i = max_i-1
        while left_i >= 0:
            while left_stk[-1][1] < height[left_i]:
                left_stk.pop()
            left_stk.append((left_i, height[left_i]))
            left_i -= 1
            
        right_stk = [(max_i, max_h)]
        right_i = max_i + 1
        while right_i < len(height):
            while right_stk[-1][1] < height[right_i]:
                right_stk.pop()
            right_stk.append((right_i, height[right_i]))
            right_i += 1
        
        res = 0
        left_wall = 0
        
        for i in range(max_i):
            if i == left_stk[-1][0]:
                _, left_wall = left_stk.pop()
                
            res += max(0, left_wall - height[i])
        
        right_wall = 0
        for i in range(len(height)-1, max_i, -1):
            if i == right_stk[-1][0]:
                _, right_wall = right_stk.pop()
            
            res += max(0, right_wall - height[i])
            
        return res

# O(n) time, O(n) space. Could be done in constant space with two pointers
