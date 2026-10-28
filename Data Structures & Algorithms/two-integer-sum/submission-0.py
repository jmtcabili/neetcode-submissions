
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        number_map = {num: index for index, num in enumerate(nums)}
        print(number_map)
        for idx, num in enumerate(nums):
            req = target - num
            if req in number_map and number_map[req] != idx:
                return [idx, number_map[req]]
            
