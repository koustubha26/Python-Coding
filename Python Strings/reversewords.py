class Solution(object):
    def reverseWords(self, s):
        rev=[]
        l=s.split()
        for word in l:
            out= rev.append(word[::-1])
        return ' '.join(rev)
