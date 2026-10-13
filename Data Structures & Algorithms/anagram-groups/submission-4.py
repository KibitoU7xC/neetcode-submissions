class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words={}
        for i in range(len(strs)):
            k="".join(sorted(strs[i]))
            if k not in words:
                words[k]=[]
            words[k].append(strs[i])
        return list(words.values())
        
            