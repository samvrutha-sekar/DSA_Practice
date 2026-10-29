class Solution:
    def celebrity(self, mat):
        n = len(mat)
        candidate = 0

        # Find a potential celebrity
        for i in range(1, n):
            if mat[candidate][i] == 1:
                candidate = i

        # Verify the candidate
        for i in range(n):
            if i != candidate:
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1

        return candidate