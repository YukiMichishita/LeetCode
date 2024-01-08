class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_appearance_cnt = {}

        for c in s:
            char_appearance_cnt[c] = char_appearance_cnt.get(c, 0) + 1

        for i, c in enumerate(s):
            if char_appearance_cnt[c] == 1:
                return i

        return -1
