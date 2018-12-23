class Solution(object):
    def maximumProduct(self, nums):
        k=sorted(nums)
        maxprod1=k[-1]*k[-2]*k[-3]
        maxprod2=k[0]*k[1]*k[-1]
        return max(maxprod1,maxprod2)
