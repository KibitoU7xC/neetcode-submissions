class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        
        # Step 1: Loop BACKWARD first to multiply all numbers AFTER 'i' (Suffixes)
        suffix = 1
        for i in range(length - 1, -1, -1):
            result[i] = suffix
            suffix *= nums[i]
            
        # Step 2: Loop FORWARD next to multiply all numbers BEFORE 'i' (Prefixes)
        prefix = 1
        for i in range(length):
            result[i] *= prefix
            prefix *= nums[i]
            
        return result