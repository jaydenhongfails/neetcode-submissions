class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {} 
        countT = {}

        for i in s:
            if i in countS:
                countS[i] += 1
            else:
                countS[i] = 1
        
        for i in t:
            if i in countT:
                countT[i] += 1
            else:
                countT[i] = 1

        return countS == countT

