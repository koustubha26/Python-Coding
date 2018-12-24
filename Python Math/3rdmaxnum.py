class Solution(object):
    def thirdMax(self, nums):
        s1=set(nums)
        nums1=list(s1)
        nums2=sorted(nums1)
        if len(nums2)>=3:
            return nums2[-3]
        else:
            return nums2[-1]
