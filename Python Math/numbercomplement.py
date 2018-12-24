class Solution(object):
    def findComplement(self, num):
        l=[]
        bin1=str(bin(num)[2:])
        for i in bin1:
            if i=='1':
                l.append('0')
            if i=='0':
                l.append('1')
        bin2=''.join(l)
        num2=int(bin2,2)
        return num2
