class Solution(object):
    def detectCapitalUse(self, word):
        up=word.upper()
        low=word.lower()
        if word==up:
            return True
        elif (word[0]==up[0]) and (word[1:]==low[1:]):
            return True
        elif word==low:
            return True
        else:
            return False
