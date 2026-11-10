class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        addends = {} #"x: index"

        for i in range(0, len(nums)):
            addend = target - nums[i]

            if addend in addends:
                index = addends[addend]
                return [index, i]
            else:
                addends[nums[i]] = i
        

