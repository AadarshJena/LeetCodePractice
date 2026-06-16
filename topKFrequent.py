class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        solutionList = []
        counter = 0
        
        for i in nums:
            hashMap[i] = 1 + hashMap.get(i, 0)
        
        #print(f"Here is the normal hashmap: {hashMap}")
        
        #print(f"Here is the maximum frequency: {max(hashMap.values())}")
        
        sortedHashMap = sorted(hashMap.items(), key = lambda pair: pair[1], reverse = True)
        #print(f"Here is the sorted hashmap: {sortedHashMap}")
            
        while counter < k:
            solutionList.append(sortedHashMap[counter][0])
            counter += 1
        return solutionList
            
            
gang = Solution()
print(gang.topKFrequent([1,2,2,2,3,2,3,2,3,3,2,3,3,3], 2))
            