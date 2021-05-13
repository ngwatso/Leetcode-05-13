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