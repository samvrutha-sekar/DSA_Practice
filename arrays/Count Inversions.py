class Solution:
    def numberOfInversions(self, nums):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, count1 = merge_sort(arr[:mid])
            right, count2 = merge_sort(arr[mid:])

            count = count1 + count2
            merged = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    count += len(left) - i
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged, count

        _, count = merge_sort(nums)
        return count
