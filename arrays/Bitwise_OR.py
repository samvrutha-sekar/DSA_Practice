
class Solution:
    def orArray(self, A):
        answer = []

        for i in range(len(A) - 1):
            answer.append(A[i] | A[i + 1])

        return answer