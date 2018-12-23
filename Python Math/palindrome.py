class Solution:
    def isPalindrome(self, x):
        n1= str(x)
        n2= n1[::-1]
        if(n1==n2):
            return True
        else:
            return False
