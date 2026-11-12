class Solution:

    def initializeHeap(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] > self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break

    def changeKey(self, index, new_val):
        if index >= len(self.heap):
            return

        old_val = self.heap[index]
        self.heap[index] = new_val

        if new_val < old_val:
            while index > 0:
                parent = (index - 1) // 2

                if self.heap[parent] > self.heap[index]:
                    self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
                    index = parent
                else:
                    break
        else:
            self.heapify(index)

    def extractMin(self):
        if len(self.heap) == 0:
            return -1

        minimum = self.heap[0]

        if len(self.heap) == 1:
            self.heap.pop()
            return minimum

        self.heap[0] = self.heap.pop()
        self.heapify(0)

        return minimum

    def isEmpty(self):
        return len(self.heap) == 0

    def getMin(self):
        if len(self.heap) == 0:
            return -1
        return self.heap[0]

    def heapSize(self):
        return len(self.heap)

    def heapify(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        n = len(self.heap)

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)