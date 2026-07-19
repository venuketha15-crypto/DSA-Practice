from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        r = len(matrix)
        c = len(matrix[0])

        firstRowZeros = False
        firstColZeros = False

        # Check if the first row originally contains a zero
        for j in range(c):
            if matrix[0][j] == 0:
                firstRowZeros = True

        # Check if the first column originally contains a zero
        for i in range(r):
            if matrix[i][0] == 0:
                firstColZeros = True

        # Use first row and first column as markers
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set inner cells to zero based on markers
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set first row to zero if it originally contained a zero
        if firstRowZeros:
            for j in range(c):
                matrix[0][j] = 0

        # Set first column to zero if it originally contained a zero
        if firstColZeros:
            for i in range(r):
                matrix[i][0] = 0
