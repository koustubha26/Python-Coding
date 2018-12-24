class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maxsum=0
        sum1=0
        for i in nums:
            if i==0:
                sum1=0
            elif i==1:
                sum1+=1
                if(sum1>maxsum):
                    maxsum=sum1
        return maxsum
