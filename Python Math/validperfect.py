class Solution:
    def isPerfectSquare(self, num):
        x=num**0.5
        y=str(x)
        print(y)
        z=y.split('.')
        if(z[1]=='0'):
            return True
        else:
            return False
