class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s2 = "".join(filter(str.isalnum, s))
        l, r = 0, len(s2)-1

        while l<r:
            if s2[l] == s2[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
            