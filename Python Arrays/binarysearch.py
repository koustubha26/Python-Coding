class Solution:
    def search(self, nums, target):
        m=list(enumerate(nums))
        for k,v in m:
            if v==target:
                return k
        if nums.count(target)==0:
            return -1
