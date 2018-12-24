class Solution(object):
    def sortArrayByParity(self, A):
        sort=[]
        for i in A:
            if i%2==0:
                sort.append(i)
        for j in A:
            if j%2!=0:
                sort.append(j)
        return sort
