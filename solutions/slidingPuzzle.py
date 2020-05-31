from queue import Queue
FINAL_STATE = ((1,2,3),(4,5,0))
DIRECTIONS = [
    (1,0),
    (0,1),
    (-1, 0),
    (0, -1),
]
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        moves = set()        
        q = Queue()
        q.put((FINAL_STATE, 0, (1, 2)))
        
        board_tup = tuple([tuple(tup) for tup in board])
        while q.qsize():
            state, score, zero_pos = q.get()
            if state in moves:
                continue
            elif state == board_tup:
                return score
            moves.add(state)
            for dr, dc in DIRECTIONS:
                zero_row, zero_col = zero_pos
                nr = zero_row + dr
                nc = zero_col + dc

                if 0 <= nr <= 1 and\
                   0 <= nc <= 2:
                    new_state = self.swap_state(state, zero_row, zero_col, nr, nc)
                    if new_state not in moves:
                        q.put((new_state, score + 1, (nr, nc)))
        return -1
        
    def swap_state(self, state, r1, c1, r2, c2):
        state = [list(tup) for tup in state]
        state[r1][c1], state[r2][c2] = state[r2][c2], state[r1][c1]
        return tuple([tuple(tup) for tup in state])

# O(1) time, as 720 possible states, each can transition to 3 others
# O(1) space
