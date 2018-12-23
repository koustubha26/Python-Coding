class Solution(object):
    def selfDividingNumbers(self, left, right):
        selfnum=[]
        for n in range(left,right+1):
            num=list(str(n))
            condcount=0
            for digit in num:
                if int(digit)!=0 and n%int(digit)==0:
                    condcount+=1
                    if condcount==len(num):
                        selfnum.append(n)
        return selfnum
