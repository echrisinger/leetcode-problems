class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        top = 0
        bottom = len(matrix) - 1
        
        starting_row = -1
        while top <= bottom:
            mid = top + (bottom-top)//2
            row = matrix[mid]
            if row[0] <= target <= row[len(row)-1]:
                starting_row = mid
                break
            elif target > row[len(row)-1]:
                top = mid+1
            else:
                bottom = mid-1
                    
        if starting_row == -1:
            return False
                
        # search all rows below starting row until not in the row
        row_idx = starting_row
        while row_idx < len(matrix) and matrix[row_idx][0] <= target <= matrix[row_idx][len(matrix[0])-1]:
            if self.binary_search(matrix[row_idx], target):
                return True
            
            row_idx += 1
        
        row_idx = starting_row - 1
        while row_idx >= 0 and matrix[row_idx][0] <= target <= matrix[row_idx][len(matrix[0])-1]:
            if self.binary_search(matrix[row_idx], target):
                return True
        
            row_idx -= 1
        
        return False

    def binary_search(self, row, target):
        start = 0
        end = len(row) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                end = mid-1
            else:
                start = mid+1
                
        return False

# O(m*log(n)) time, O(1) space
