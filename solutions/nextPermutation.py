from collections import defaultdict

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return nums
        
        for i in range(len(nums)-2, -1, -1):
            n = nums[i]
            prev = nums[i+1]
            if n < prev:
                start_swap = i+1
                next_num = start_swap
                for j in range(start_swap, len(nums)):
                    n = nums[j]
                    if n <= nums[i]:
                        break
                    next_num = j
                nums[next_num], nums[i] = nums[i], nums[next_num]
                end_swap = len(nums) - 1
                while start_swap < end_swap:
                    nums[start_swap], nums[end_swap] = nums[end_swap], nums[start_swap]
                    start_swap += 1
                    end_swap -= 1
                return
                
        nums.reverse()
        return
        
# O(n) time, O(1) space
