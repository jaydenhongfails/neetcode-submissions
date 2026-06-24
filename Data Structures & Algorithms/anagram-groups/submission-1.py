class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sub = {}

        for char in strs:
            key = "".join(sorted(char))
            if key in sub:
                sub[key].append(char)
            else:
                sub[key] = [char]

        return list(sub.values())