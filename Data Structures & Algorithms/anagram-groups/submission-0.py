from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dic = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagram_dic[sorted_s].append(s)
        return list(anagram_dic.values())