# (it, it)     (it, n - 1 - it)
# 1  2  3  4  5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9 (n - 1 - it, n - 1 - it)
# (n - 1 - it, it)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [
            [-1]*n
            for _ in range(n)
        ]
        curr = 1
        return self.helper(curr, matrix, 0)
            
    def helper(self, curr, matrix, iteration):
        base_case = len(matrix)//2
        if iteration == base_case:
            if len(matrix) % 2:
                matrix[iteration][iteration] = curr
            return matrix
        
        final_rc = len(matrix)-1-iteration
        for col in range(iteration, final_rc):
            matrix[iteration][col] = curr
            curr += 1
        
        for row in range(iteration, final_rc):
            matrix[row][final_rc] = curr
            curr += 1
        
        for col in range(final_rc, iteration, -1):
            matrix[final_rc][col] = curr
            curr += 1
        
        for row in range(final_rc, iteration, -1):
            matrix[row][iteration] = curr
            curr += 1
        
        return self.helper(curr, matrix, iteration + 1)
            
# O(n) time, O(n^2) space.
