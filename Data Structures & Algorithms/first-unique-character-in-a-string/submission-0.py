class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        count = 0

        for index, char in enumerate(s):
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] +=1
        
        for index, char in enumerate(s):
            if seen[char] == 1:
                return index

        return -1