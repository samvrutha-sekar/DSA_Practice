class Solution:
    def maxMeetings(self, start, end):
        n = len(start)

        meetings = []

        for i in range(n):
            meetings.append((end[i], start[i]))

        meetings.sort()

        count = 0
        last_end = -1

        for e, s in meetings:
            if s > last_end:
                count += 1
                last_end = e

        return count