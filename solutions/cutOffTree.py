MOVES = [
    (1,0),
    (0,1),
    (-1,0),
    (0, -1)
]

from queue import PriorityQueue, SimpleQueue

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        trees = PriorityQueue()
        for r in range(len(forest)):
            for c in range(len(forest[0])):
                if forest[r][c] > 1:
                    trees.put((forest[r][c], r, c))
        
        curr_r, curr_c = 0, 0
        moves = 0
        while trees.qsize():
            _, r, c = trees.get()
            path_moves = self.bfs(forest, r, c, curr_r, curr_c)
            if path_moves == -1:
                return -1
            
            moves += path_moves
            curr_r, curr_c = r,c
            
        return moves
    
    def bfs(self, forest, dst_r, dst_c, curr_r, curr_c):
        queue = SimpleQueue()
        queue.put((0, curr_r, curr_c))
        
        seen = set()
        while queue.qsize():
            move_count, r, c = queue.get()
            
            if (r, c) in seen:
                continue
            seen.add((r,c))
            
            if r == dst_r and c == dst_c:
                return move_count
            
            for r_d, c_d in MOVES:
                n_r = r + r_d
                n_c = c + c_d
                if 0 <= n_r < len(forest) and\
                   0 <= n_c < len(forest[0]) and\
                   forest[n_r][n_c] >= 1:
                    queue.put((move_count+1, n_r, n_c))
            
        return -1

# O(n^2) time, O(n) space)
