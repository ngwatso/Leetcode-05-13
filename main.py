class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftSum = 0
        revSum = 0

        for i, num in enumerate(nums):
            revSum = sum(nums[(i+1):])
            if i > 0:
                leftSum = sum(nums[:i])
            else:
                leftSum = 0
            if leftSum == revSum:
                return i
            else:
                continue

        return -1         
        
'''

U:

[1, 7, 3, 6, 5, 6]
output = 3

[5, 2, 1, 4]
output = 1

[1, 3, 4]
output = -1

[]
output = -1

P:

iterate through list forwards and backwards, sum indexes, once sums are the same, give remaining index.  If no solution, return -1

'''

# =========================================

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1

        for i, num in enumerate(digits):
            j = -(i+1)
            while j >= len(digits) * -1 and j != 0:
                if digits[j] == 9 and carry == 1:
                    digits[j] = 0
                    carry = 1
                else:
                    digits[j] = digits[j] + carry
                    carry = 0
                j -= 1
            if carry == 1:
                digits.insert(0, 1)
                return digits
            else:
                return digits
        
'''

U:

[1, 2, 3]
output = [1, 2, 4]

[9, 9]
output = [1, 0, 0]

P:

create carry variable, set at 1, iterate in reverse through list, adding carry to i.  if i = 10, set i to 0 and carry to 1.  If i = 0 and carry = 1, insert carry at i = 0.

'''