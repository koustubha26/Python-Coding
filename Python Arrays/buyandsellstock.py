class Solution:
    def maxProfit(self, prices):
        porl=[]
        maxprofit=0
        for i in range(0,len(prices)-1):
            diff=prices[i+1]-prices[i]
            porl.append(diff)
        for j in porl:
            if j>0:
                maxprofit=maxprofit+j
        return maxprofit
