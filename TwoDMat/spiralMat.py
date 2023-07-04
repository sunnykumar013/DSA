class Solution(object):
    def spiralOrder(self, matrix):

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        down = len(matrix) - 1

        res = []

        while (top <= down and left <= right):

            for i in range(left, right + 1):
                res.append(matrix[left][i])

            top += 1

            for i in range(top, down + 1):
                res.append(matrix[i][right])

            right -= 1

            if (top <= down):
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])

                down -= 1

            if (left <= right):
                for i in range(down, top - 1, -1):
                    res.append(matrix[i][left])

                left += 1
        return res


