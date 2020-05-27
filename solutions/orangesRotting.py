from collections import Counter

MOVES = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_counts = [Counter(row) for row in grid]
        total_oranges = sum([c[1] + c[2] for c in row_counts])
        
        rotten_count = 0
        to_rot = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten_count += 1
                    for rd, cd in MOVES:
                        nr = r + rd
                        nc = c + cd
                        if 0 <= nr < len(grid) and\
                           0 <= nc < len(grid[0]) and\
                           grid[nr][nc] == 1:
                            to_rot.append((nr, nc))
                        
        num_iterations = 0
        while to_rot:
            for r, c in to_rot:
                if grid[r][c] == 2:
                    continue
                    
                grid[r][c] = 2
                rotten_count += 1
            
            next_to_rot = set()
            for r, c in to_rot:
                for rd, cd in MOVES:
                    nr = r + rd
                    nc = c + cd
                    if 0 <= nr < len(grid) and\
                       0 <= nc < len(grid[0]) and\
                       grid[nr][nc] == 1:
                        next_to_rot.add((nr, nc))
            
            to_rot = list(next_to_rot)
            num_iterations += 1
        
        print(rotten_count)
        return max(0, num_iterations) if rotten_count == total_oranges else -1

