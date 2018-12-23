class Solution(object):
    def reverse(self,x):
        y=abs(x)
        z=str(y)[::-1]
        w=-int(z)
        global result
        
        if x==0:
            result=0
        elif x*y>0:
            if int(z)<=((2**31))-1:
                result=int(z)
            else:
                result=0
        
        elif x*y<0:
            if int(w)>=(-2)**31:
                result=int(w)
            else:
                result=0
                
        return result
