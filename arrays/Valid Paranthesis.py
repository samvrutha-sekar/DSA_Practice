class Solution:
    def checkValidString(self, s):
        open = []
        star = []

        for i, ch in enumerate(s):
            if ch == '(':
                open.append(i)

            elif ch == '*':
                star.append(i)

            else:
                if open:
                    open.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while open and star:
            if open[-1] > star[-1]:
                return False

            open.pop()
            star.pop()

        return len(open) == 0
