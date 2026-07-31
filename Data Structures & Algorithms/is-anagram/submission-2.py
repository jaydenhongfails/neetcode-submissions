class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sortS = "".join(sorted(s))
        sortT = "".join(sorted(t))

        return sortS == sortT