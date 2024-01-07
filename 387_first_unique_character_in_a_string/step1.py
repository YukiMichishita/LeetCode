class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_appearance = {}

        for i, c in enumerate(s):
            if c not in char_appearance.keys():
                char_appearance[c] = i
            else:
                char_appearance[c] = 10 ** 6

        answer = min(char_appearance.values())
        if answer == 10 ** 6:
            return -1
        return answer
