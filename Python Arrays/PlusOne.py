class Solution(object):
    def plusOne(self, digits):
        l=[]
        final=[]
        for i in digits:
            l.append(str(i))
        strnum=''.join(l)
        num1=int(strnum)+1
        m=list(str(num1))
        for j in m:
            final.append(int(j))
        return final
