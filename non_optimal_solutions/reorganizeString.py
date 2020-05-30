from queue import PriorityQueue

class Solution:
    def reorganizeString(self, S: str) -> str:
        counts = Counter(S)
        
        pq = PriorityQueue()
        for c, count in counts.items():
            pq.put((-count, c))
            
        res = []
        while pq.qsize():
            count, c = pq.get()
            if not res or res[-1] != c:
                res.append(c)
                if count != -1:
                    pq.put((count+1, c))
            else:
                if not pq.qsize():
                    return ''
                n_count, n_c = pq.get()
                res.append(n_c)
                if n_count != -1:
                    pq.put((n_count+1, n_c))
                
                pq.put((count, c))
        
        return ''.join(res)

# O(n log n)
