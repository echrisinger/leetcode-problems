class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        wide_nums = {}
        thin_nums = {}
        wide = thin = 0
        count = 0
        
        for i in range(len(A)):
            n = A[i]
            if n not in wide_nums:
                wide_nums[n] = 0
            
            if n not in thin_nums:
                thin_nums[n] = 0
                
            wide_nums[n] += 1
            thin_nums[n] += 1
            
            while len(wide_nums) > K:
                wide_n = A[wide]
                wide_nums[wide_n] -= 1
                if not wide_nums[wide_n]:
                    del wide_nums[wide_n]
                
                wide += 1
            
            while len(thin_nums) >= K:
                thin_n = A[thin]
                if thin_nums[thin_n] == 1 and len(thin_nums) == K:
                    break
                    
                thin_nums[thin_n] -= 1
                if not thin_nums[thin_n]:
                    del thin_nums[thin_n]
                
                thin += 1
            
            if len(thin_nums) == K and len(wide_nums) == K:
                count += (thin - wide) + 1
        
        return count

# O(n) time, O(n) space

