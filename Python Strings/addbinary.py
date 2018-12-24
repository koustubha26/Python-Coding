class Solution:
    def addBinary(self, a, b):
        bin1=int(a,2)
        bin2=int(b,2)
        sum=bin1+bin2
        return str(bin(sum)[2:])
