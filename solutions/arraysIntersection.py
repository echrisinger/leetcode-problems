from collections import Counter

# [1, 2, 4]
# [2, 4, 5]
# [2, 6, 7]
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        new_arr = []
        i1 = i2 = i3 = 0
        while i1 < len(arr1) and i2 < len(arr2) and i3 < len(arr3):
            all_elements = [arr1[i1], arr2[i2], arr3[i3]]
            if all(arr1[i1] == e for e in all_elements) and (not len(new_arr) or arr1[i1] != new_arr[-1]):
                new_arr.append(arr1[i1])
                i1 += 1
                i2 += 1
                i3 += 1
            elif arr1[i1] == min(all_elements):
                i1 += 1
            elif arr2[i2] == min(all_elements):
                i2 += 1
            else:
                i3 += 1
        
        return new_arr

