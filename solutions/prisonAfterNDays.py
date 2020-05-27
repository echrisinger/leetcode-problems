class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        state_transitions = {}
        for i in range(2**8):
            i_cells = self.to_cell(i)
            next_cells = self.evolve(i_cells)
            state_transitions[tuple(i_cells)] = tuple(next_cells)
        
        state = tuple(cells)
        prev_states = {}
        day = 0
        while day < N:
            if state in prev_states:
                prev_day = prev_states[state]
                date_diff = day - prev_day
                num_skips = (N - day) // date_diff
                day += num_skips * date_diff
                prev_states[state] = day
            else:
                prev_states[state] = day
                
            if day < N:
                state = state_transitions[state]
                day += 1
    
        return list(state)
    
    def to_cell(self, i: int) -> List[int]:
        res = []
        for shift in range(7, -1, -1):
            mask = 1 << shift
            val = (i & mask) >> shift
            res.append(val)
        return res
            
    def evolve(self, cells: List[int]) -> List[int]:
        next_cells = [0]
        for i in range(1, 7):
            left = cells[i-1]
            right = cells[i+1]
            next_cells.append(int(not (left ^ right)))
            
        next_cells.append(0)
        return next_cells

# O(1) space, as there are 256 entries in state_transitions
# and 256 entries max in prev_states. O(1) time, as after
# 256 entries, you'll run into a cycle, and then you can
# skip ahead the number of cycles that fit into the remainder
# then just perform the rest (with some skips possible)

# after looking at the answers, it looks like you can do this
# in 2^6 space, as the outsides will always be 0. Derp

