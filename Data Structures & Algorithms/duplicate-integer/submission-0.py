class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #define map
        map = {}
        for num in (nums):
            #if map does not have val
            if num not in map:
                map[num] = 1
            else:
                return True
        return False

        