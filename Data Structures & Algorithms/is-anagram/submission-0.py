class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = tuple(sorted(s))
        t_sorted = tuple(sorted(t))
        if s_sorted == t_sorted:
            return True
        else:
            return False