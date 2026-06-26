class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for i in s:
            if i.isalnum():
                arr.append(i.lower())

        left = 0
        right = len(arr) - 1

        while left < right:
            if arr[left] == arr[right]:
                left = left+1
                right = right-1
            else:
                return False
        return True