class Solution(object):
    def moveZeroes(self, nums):
        k=nums.count(0)
        for i in range(0,k):
            nums.remove(0)
        for j in range(0,k):
            nums.append(0)
