class Solution(object):
    def convertToBase7(self, num):
        list1=[]
        n=abs(num)
        while n>6:
            rem=n%7
            n=n//7
            list1.append(str(rem))
        list1.append(str(n))
        list7=list1[::-1]
        if num>=0:
            return "".join(list7)
        if num<0:
            return "-"+"".join(list7)
