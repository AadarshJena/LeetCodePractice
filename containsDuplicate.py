class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashMap = {}
        for num in nums:
            if hashMap.get(num, 0) != 0:
                return True
            
            hashMap[num] = 1 + hashMap.get(num, 0)
            
        return False
    
    
gang = Solution()
print(gang.hasDuplicate([1,2,3,3]))