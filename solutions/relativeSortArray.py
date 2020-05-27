from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = Counter(arr1)
        arr1_idx = 0
        for i in arr2:
            count = counts[i]
            while count != 0:
                arr1[arr1_idx] = i
                arr1_idx += 1
                count -= 1
            
            del counts[i]
        
        sorted_keys = sorted(counts.keys())
        for i in sorted_keys:
            count = counts[i]
            while count != 0:
                arr1[arr1_idx] = i
                arr1_idx += 1
                count -= 1
            
        return arr1

