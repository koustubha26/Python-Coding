class Solution:
    def hammingDistance(self, x, y):
        bin1='{0:031b}'.format(x)
        bin2='{0:031b}'.format(y)
        l1=list(bin1)
        l2=list(bin2)
        hammingd=0
        for i in range(len(l1)):
            for j in range(len(l2)):
                if i==j:
                    if l1[i]!=l2[j]:
                        hammingd+=1
        return hammingd
