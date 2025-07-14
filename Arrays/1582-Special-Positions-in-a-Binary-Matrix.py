class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        col = len(mat[0])

        row_sum = [sum(row) for row in mat]
        col_sum = [sum(mat[i][j]for i in range(rows))for j in range(col)]

        count = 0
        for i in range(rows):
            for j in range(col):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    count += 1
        return count 