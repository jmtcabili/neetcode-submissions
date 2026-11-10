from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        if not counts:
            return False
        if (max(counts.values()) > 1):
            return True
        else: return False
        