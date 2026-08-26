class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = []
        used = set()
        res= []

        def search():
            if len(curr) == len(nums):
                res.append(list(curr))
                return

            for n in nums:
                if n not in used:
                    curr.append(n)
                    used.add(n)
                    search()
                    curr.pop()
                    used.remove(n)

        search()
        return res