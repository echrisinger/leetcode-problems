class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        table = [0]*(target+1)
        table[0] = 1
        
        for curr_d in range(1, d+1):
            for t in range(target, -1, -1):
                val = 0
                for roll in range(1, f+1):
                    next_target = t - roll
                    if next_target < 0:
                        break
                    
                    val += table[next_target]
                
                table[t] = val
        
        return table[target] % (10**9 + 7)

