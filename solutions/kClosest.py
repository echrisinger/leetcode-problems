from queue import PriorityQueue

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        max_heap = PriorityQueue()
        for x, y in points[:K]:
            euc_dist = self.get_euc(x, y)
            max_heap.put((-euc_dist, (x,y)))
            
        for x, y in points[K:]:
            euc_dist = self.get_euc(x, y)
            if max_heap.queue[0][0] < -euc_dist:
                max_heap.put((-euc_dist, (x,y)))
                max_heap.get()
                
        return [list(entry[1]) for entry in max_heap.queue]
            
    def get_euc(self, x, y):
        return (x**2 + y**2)**(1/2)

