class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        def backtrack(row, columns, diagonals, anti_diagonals, current_board):
            if row == n:
                res.append(current_board[:])
                return
            
            for col in range(n):
                if col in columns or (row - col) in diagonals or (row + col) in anti_diagonals:
                    continue
                
                columns.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)
                current_board.append('.' * col + 'Q' + '.' * (n - col - 1))

                backtrack(row + 1, columns, diagonals, anti_diagonals, current_board)
                
                columns.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)
                current_board.pop()
        
        backtrack(0, set(), set(), set(), [])
        return res
