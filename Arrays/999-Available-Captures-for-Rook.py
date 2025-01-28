class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rook_row,rook_col = i,j
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        captures = 0

        for dr,dc in directions:
            r,c = rook_row,rook_col

            while 0<=r+dr<8 and 0<=c+dc<8:
                r+=dr
                c+=dc

                if board[r][c] == 'B':
                    break
                if board[r][c] == 'p':
                    captures+=1
                    break
        return captures