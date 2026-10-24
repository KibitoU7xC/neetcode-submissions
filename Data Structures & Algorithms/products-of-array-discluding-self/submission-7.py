class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        
        # Step 1: Calculate prefix products
        # Each element at index i will store the product of all elements before i
        prefix = 1
        for i in range(length):
            result[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate suffix products on the fly
        # Multiply each prefix product by the corresponding suffix product
        suffix = 1
        for i in range(length - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
            
        return result
