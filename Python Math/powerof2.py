from math import log
class Solution:
    def isPowerOfTwo(self, n):
        if n>0:
            k=math.log(n,2)
            str1=str(k)
            str2=str1.split('.')
            if str2[1]=='0':
                return True
            else:
                return False
        else:
            return False
