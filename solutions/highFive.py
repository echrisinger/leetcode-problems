from collections import defaultdict
from queue import PriorityQueue

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        student_top_five_scores = defaultdict(PriorityQueue)
        
        for student, score in items:
            pq = student_top_five_scores[student]
            pq.put(score)
            if pq.qsize() > 5:
                pq.get()
        
        return [
            [student, sum(pq.queue)//pq.qsize()]
            for student, pq in student_top_five_scores.items()
        ]
    
# O(N) time, as each PQ has five entries max.
# O(N) space, as worst case is each student has exactly 5 scores.

