class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ki={}
        for i in range(len(nums)):
            if nums[i] not in ki:
                ki[nums[i]]=0
            ki[nums[i]]=ki[nums[i]]+1

        return sorted(ki,key=ki.get,reverse=True)[:k]