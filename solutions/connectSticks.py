from queue import PriorityQueue

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        pq = PriorityQueue()
        for stick in sticks:
            pq.put(stick)
            
        total = 0
        while pq.qsize() > 1:
            new_stick = pq.get() + pq.get()
            total += new_stick
            pq.put(new_stick)
        
        return total

# O(n*log(n)), as initial sort is nlogn and there are
# at most log n elements traversed in the heap on re-
# insertion. We connect sticks n-1 times.
# O(n) space.
