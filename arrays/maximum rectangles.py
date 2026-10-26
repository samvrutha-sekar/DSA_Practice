class Solution:
    def maximalAreaOfSubMatrixOfAll1(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 or matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []

            for j in range(cols + 1):
                curr_height = heights[j] if j < cols else 0

                while stack and heights[stack[-1]] > curr_height:
                    height = heights[stack.pop()]

                    if stack:
                        width = j - stack[-1] - 1
                    else:
                        width = j

                    max_area = max(max_area, height * width)

                stack.append(j)

        return max_area