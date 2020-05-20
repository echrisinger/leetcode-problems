class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_jumps = 0
        curr_max_jump = 0
        next_max_jump = -float('inf')
        for i, n in enumerate(nums):
            if i > curr_max_jump:
                curr_jumps += 1
                curr_max_jump = next_max_jump
            nums[i] = curr_jumps
            next_max_jump = max(next_max_jump, i+n)
        
        return nums[len(nums)-1]

