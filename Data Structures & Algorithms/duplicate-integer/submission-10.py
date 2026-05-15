class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         dict = set(nums)
         return (len(dict) != len(nums))