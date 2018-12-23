class Solution(object):
    def checkPerfectNumber(self, num):
        import math as math
        answer=[]
        x=1
        if num<=1:
            return False
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                x=x+i+num/i
        if num==x:
            return True
        else:
            return False
