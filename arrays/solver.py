
class Solution:
    def solveSudoku(self, board):
        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for num in "123456789":
                            if self.isValid(board, i, j, num):
                                board[i][j] = num

                                if solve():
                                    return True

                                board[i][j] = "."

                        return False
            return True

        solve()

    def isValid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num:
                return False

            if board[i][col] == num:
                return False

            box_row = 3 * (row // 3) + i // 3
            box_col = 3 * (col // 3) + i % 3

            if board[box_row][box_col] == num:
                return False

        return True
