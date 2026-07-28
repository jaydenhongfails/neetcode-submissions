class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        ret = []

        for n in range(1, len(nums)+1):
            if n not in nums:
                ret.append(n)
        
        return ret
            
