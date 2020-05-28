class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x11, y11, x12, y12 = rec1
        x21, y21, x22, y22 = rec2
        
        left, right = sorted([(x11, x12), (x21, x22)])
        top, bottom = sorted([(y11, y12), (y21, y22)])
        
        print(left, right)
        print(top, bottom)
        if right[0] < left[1] and\
           bottom[0] < top[1]:
                return all([tup[0] != tup[1] for tup in [top, bottom, left, right]])
            
        return False

# O(1) space, time
