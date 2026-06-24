class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index = 0
        otherIndex = 0
        answer = []
        realLength = len(nums) - 1
        
        for index in range(realLength):
            adder = 1
            while index + adder <= realLength:
                if nums[index] + nums[index + adder] == target:
                    answer.append(index)
                    answer.append(index + adder)
                    return answer
                else:
                    adder +=1 
                    continue


            
            


nums = [3, 2, 4]
print(Solution().twoSum(nums, 6))

