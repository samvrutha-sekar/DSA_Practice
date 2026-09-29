class Solution:
    def maxScore(self, cardScore, k):
        n = len(cardScore)

        total = sum(cardScore)

        window_size = n - k

        window_sum = sum(cardScore[:window_size])
        min_window = window_sum

        for i in range(window_size, n):
            window_sum += cardScore[i]
            window_sum -= cardScore[i - window_size]

            min_window = min(min_window, window_sum)

        return total - min_window
