class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x={}
        y={}
        if len(s)!=len(t):
            return False
        else:
            for i in range(len(s)):
                char=s[i]
                if s[i] in x:
                    x[char] = x[char] + 1
                else:
                    x[char]=1
            for i in range(len(t)):
                char=t[i]
                if t[i] in y:
                    y[char] = y[char] + 1
                else:
                    y[char]=1

        if x == y:
            return True
        else:
            return False


