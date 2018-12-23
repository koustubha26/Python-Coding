class Solution(object):
    def fizzBuzz(self, n):
        listofn=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                listofn.append("FizzBuzz")
            elif i%3==0:
                listofn.append("Fizz")
            elif i%5==0:
                listofn.append("Buzz")
            else:
                listofn.append(str(i))
        return listofn
