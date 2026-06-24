class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        #return 3
    
        consecutive_is_present = True
        maximum = 1
        current_streak = 1

        if len(nums ) == 0:
            return 0

        for num in nums:
            print(f"here is num: {num}")
            next_num = num + 1
            print(f"here is next_num: {next_num}")

            while consecutive_is_present:
                
                if next_num in nums:
                    consecutive_is_present = True
                    print(f"next num ({next_num}) is present in the list")
                    current_streak += 1
                    print(f"here is current_streak: {current_streak}")
                    next_num += 1
                elif next_num not in nums:
                    consecutive_is_present = False
                    print(f"next num ({next_num}) is not present in the list")
                    #maximum = max(maximum)

            maximum = max(maximum, current_streak)  
            print(f"here is maximum: {maximum}")
            print("=" * 25)      

        return maximum


gang = Solution()
print(gang.longestConsecutive([0, -1]))

if 0 in [0,-1]:
    print("True")        

        





