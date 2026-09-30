class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = dict()
        for st in strs:
            key = self.count_char(st)
            store.setdefault(key, []).append(st)
        return list(store.values())

    def count_char(self, s):
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        return tuple(counts)