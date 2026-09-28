class Solution:
    def median(self, arr1, arr2):

        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        n1 = len(arr1)
        n2 = len(arr2)

        low = 0
        high = n1

        while low <= high:

            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1

            if cut1 == 0:
                left1 = float('-inf')
            else:
                left1 = arr1[cut1 - 1]

            if cut1 == n1:
                right1 = float('inf')
            else:
                right1 = arr1[cut1]

            if cut2 == 0:
                left2 = float('-inf')
            else:
                left2 = arr2[cut2 - 1]

            if cut2 == n2:
                right2 = float('inf')
            else:
                right2 = arr2[cut2]

            if left1 <= right2 and left2 <= right1:

                if (n1 + n2) % 2 == 1:
                    return max(left1, left2)

                return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                high = cut1 - 1

            else:
                low = cut1 + 1