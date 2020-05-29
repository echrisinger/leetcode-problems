class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        
        A.sort()
        
        asc_idx = 0
        dsc_idx = len(A)-1
        res = -1
        while asc_idx < dsc_idx:
            total = A[asc_idx] + A[dsc_idx]
            if total < K:
                res = max(total, res)
            
            if total < K:
                asc_idx += 1
            else:
                dsc_idx -= 1
        
        return res

# O(nlogn), O(1)
