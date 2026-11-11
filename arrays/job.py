
class Solution:
    def JobScheduling(self, Jobs):
        Jobs.sort(key=lambda x: x[2], reverse=True)

        max_deadline = max(job[1] for job in Jobs)
        slots = [-1] * (max_deadline + 1)

        count = 0
        max_profit = 0

        for job in Jobs:
            job_id = job[0]
            deadline = job[1]
            profit = job[2]

            for j in range(deadline, 0, -1):
                if slots[j] == -1:
                    slots[j] = job_id
                    count += 1
                    max_profit += profit
                    break

        return [count, max_profit]
