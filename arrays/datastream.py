import heapq

class MedianFinder:
    def __init__(self):
        self.left = []   # Max Heap
        self.right = []  # Min Heap

    def addNum(self, num):
        heapq.heappush(self.left, -num)

        heapq.heappush(self.right, -heapq.heappop(self.left))

        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        if len(self.left) > len(self.right):
            return -self.left[0]

        return (-self.left[0] + self.right[0]) / 2