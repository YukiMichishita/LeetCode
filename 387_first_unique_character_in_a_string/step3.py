class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_occurrence_cnt = {}
        for c in s:
            char_occurrence_cnt[c] = char_occurrence_cnt.get(c, 0) + 1
        for i, c in enumerate(s):
            if char_occurrence_cnt[c] == 1:
                return i

        return -1
