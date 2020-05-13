from queue import PriorityQueue

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # use a stack to construct the unmatched items,
        # pull off items until you hit an item that is larger than the current
        # implying stack is in descending order (assuming array implementation)
        nums1_set = { 
            n: i
            for i, n in enumerate(nums1)
        }
        unmatched_nums1 = PriorityQueue()
        for n in nums2:
            if n in nums1_set:
                unmatched_nums1.put(n)
            
            while unmatched_nums1.qsize() and unmatched_nums1.queue[0] < n:
                smaller_n = unmatched_nums1.get()
                replace_index = nums1_set[smaller_n]
                nums1[replace_index] = n
            
        while unmatched_nums1.qsize():
            unmatched_n = unmatched_nums1.get()
            replace_index = nums1_set[unmatched_n]
            nums1[replace_index] = -1
        
        return nums1
        
