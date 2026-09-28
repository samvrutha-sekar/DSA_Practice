class Solution:

    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """

        teams = [str(i) for i in range(1, n + 1)]

        while len(teams) > 1:
            new_round = []

            for i in range(len(teams) // 2):
                match = "(" + teams[i] + "," + teams[-1 - i] + ")"
                new_round.append(match)

            teams = new_round

        return teams[0]