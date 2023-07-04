class Solution(object):
    def setZeroes(self, matrix):
        rows = len(matrix)
        colmn = len(matrix[0])
        rowZero = False

        for r in range(rows):
            for c in range(colmn):

                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r > 0:
                        matrix[r][0] = 0

                    else:
                        rowZero = True

        for r in range(1, rows):

            for c in range(1, colmn):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if rowZero:
            for c in range(colmn):
                matrix[0][c] = 0

        return matrix

