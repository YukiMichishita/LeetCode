from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars_to_anagrams = defaultdict(list)
        for s in strs:
            key = str(sorted(s))
            chars_to_anagrams[key].append(s)
        return [anagrams for _, anagrams in chars_to_anagrams.items()]
