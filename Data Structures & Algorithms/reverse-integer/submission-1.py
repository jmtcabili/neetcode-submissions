MAX = 2**31-1
MIN = -MAX-1
class Solution:
    def reverse(self, x: int) -> int:
        isNeg = x < 0
        num = str(x)
        if isNeg:
            num = num[1:]
        num = num[::-1]

        num = -(int (num)) if isNeg else int(num)
        if num > MAX or num < MIN:
            return 0
        else:
            return num