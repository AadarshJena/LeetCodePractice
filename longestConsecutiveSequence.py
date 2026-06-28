class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #return 3

        if len(nums) ==0:
            return 0

        max_streak = 1
        

        for num in nums:
            i = 1
            #print(f"Here is num: {num}")
            current_streak = 1
            next_num = num + 1
            #print(f"Here is next num: {next_num}")

            if next_num in nums:
                consecutive_is_present = True
                #print(f"There is a consecutive present")
                current_streak += 1
            else:
                consecutive_is_present = False
                #print(f"There is no consecutive present")
                #print("=" * 50)

            while consecutive_is_present:
                if next_num + i in nums:
                    current_streak +=1
                    #print(f"{next_num+i} is in nums")
                    #print(f"Current streak: {current_streak}")
                    i+=1
                else:
                    #print(f"{next_num+i} is not in nums")
                    consecutive_is_present = False
                    max_streak = max(current_streak, max_streak)
        #print("=" * 50)
        return max_streak

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """maximum = 1
        current_streak = 1

        if len(nums ) == 0:
            return 0

        for num in nums:
            consecutive_is_present = True
            #print(f"here is num: {num}")
            next_num = num + 1
            #print(f"here is next_num: {next_num}")

            while consecutive_is_present:
                
                if next_num in nums:
                    consecutive_is_present = True
                    #print(f"next num ({next_num}) is present in the list")
                    current_streak += 1
                    #print(f"here is current_streak: {current_streak}")
                    next_num += 1
                elif next_num not in nums:
                    consecutive_is_present = False
                    #print(f"next num ({next_num}) is not present in the list")
                    maximum = max(maximum, current_streak)

            maximum = max(maximum, current_streak)  
            #print(f"here is maximum: {maximum}")
            #print("=" * 25)      

        return maximum"""


gang = Solution()
print(gang.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))

"""if 0 in [0,-1]:
    print("True")   """     

        





