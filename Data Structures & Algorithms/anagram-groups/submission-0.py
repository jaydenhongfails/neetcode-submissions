class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sub = {}

        for i in range(len(strs)):
            word = strs[i]
            key = "".join(sorted(word))

            if key in sub:
                sub[key].append(word)
            else:
                sub[key] = []
                sub[key].append(word)
            
        return list(sub.values())

                