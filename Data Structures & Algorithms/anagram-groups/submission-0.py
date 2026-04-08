class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            cnt = [0] * 26
            for c in i:
                cnt[ord(c) - ord("a")] += 1

            res[tuple(cnt)].append(i)
        return res.values()