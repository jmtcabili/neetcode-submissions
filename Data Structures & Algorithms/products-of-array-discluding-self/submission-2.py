import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            Case:
                1 zero -> everything in the arr is 0 but ans[i] where i such that nums[i] == 0
                >=2 zero -> everything guaranteed 0
        """

        count_0 = nums.count(0)
        if count_0 >= 1: 
            ans = [0 for num in nums]
            if count_0 > 1:
                return ans
            else: 
                nums_no_0 = [num for num in nums if num != 0]
                prod = math.prod(nums_no_0)
                ans[nums.index(0)] = prod
                return ans
        else:
            prod = math.prod(nums)
            ans = []
            for num in nums:
                ans.append(prod//num)
            return ans

        



        



        

        