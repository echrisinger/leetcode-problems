MOVES = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1),
    (1,1),
    (1,-1),
    (-1,-1),
    (-1,1),
]

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                # Dead => Dead - 2
                # Dead => Live - 3
                
                # Live => Live - 5
                # Live => Dead - 4
                live_neighbors = 0
                for rd, cd in MOVES:
                    nr = r + rd
                    nc = c + cd
                    if 0 <= nr < len(board) and\
                       0 <= nc < len(board[0]):
                        if board[nr][nc] in range(2, 6):
                            live_neighbors += board[nr][nc] // 2 - 1
                        else:
                            live_neighbors += board[nr][nc]
                
                if board[r][c] and (live_neighbors < 2 or live_neighbors > 3):
                    board[r][c] = 4
                elif board[r][c]:
                    board[r][c] = 5
                elif live_neighbors == 3:
                    board[r][c] = 3
                else:
                    board[r][c] = 2
                
        print(board)
        for r in range(len(board)):
            for c in range(len(board[0])):
                board[r][c] %= 2

# O(n) time, O(1) space
