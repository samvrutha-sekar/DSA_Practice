class Solution:

    def capitalize_first_last(self, s: str) -> str:
        words = s.split()

        for i in range(len(words)):
            word = words[i]

            if len(word) == 1:
                words[i] = word.upper()
            else:
                words[i] = word[0].upper() + word[1:-1] + word[-1].upper()

        return " ".join(words)