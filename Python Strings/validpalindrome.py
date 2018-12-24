class Solution(object):
    def isPalindrome(self, s):
        slower=s.lower()
        sfinal=""
        for i in slower:
            if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):
                sfinal=sfinal+i
        if sfinal[::-1]==sfinal:
            return True
        else:
            return False
