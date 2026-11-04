class Solution:
    def findPlatform(self, Arrival, Departure):
        Arrival.sort()
        Departure.sort()

        n = len(Arrival)
        i = 0
        j = 0

        platforms = 0
        max_platforms = 0

        while i < n:
            if Arrival[i] <= Departure[j]:
                platforms += 1
                max_platforms = max(max_platforms, platforms)
                i += 1
            else:
                platforms -= 1
                j += 1

        return max_platforms