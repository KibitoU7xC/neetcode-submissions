class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x={}
        y={}
        for i in s:
            if i not in x:
                x[i]=1;
            else:
                x[i]=x[i]+1
        for i in t:
            if i not in y:
                y[i]=1;
            else:
                y[i]=y[i]+1
        if x==y:
            return True
        else:
            return False