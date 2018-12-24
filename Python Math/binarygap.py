class Solution(object):
    def binaryGap(self, N):
        indices=[]
        diff=[]
        n=str(bin(int(N)))[2:]
        for i in range(0,len(n)):
            if(n[i]=='1'):
                indices.append(i)
        if(len(indices)==1 or len(indices)==0):
            return 0
        else:
            for j in range(0,len(indices)-1):
                diff.append(indices[j+1]-indices[j])
            return max(diff)
