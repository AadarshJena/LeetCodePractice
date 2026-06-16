class Solution:
    def maxSubarraySum(self, arr):
        #code here
        '''
        -Find all possible subarrays
        -Organize them in a dictionary where key=subarray and value = sum of nums in subarray
        -Go through the values and find the max
        -Output the key
        
        '''
        sum_dict = {}
        #subarrays: min is 1 number, max is length of the base array
        length = len(arr)
        num_subarrays = ((length +1) * length)/2
        
        
        lengthOfSubarray=1  #starts as one, goes until it's the length of the base array
        idx_last = 0       #the last index used to slice the base array
        
        max_sum = -999999999999999
        
        while lengthOfSubarray <= length:
            idx_first = 0
            idx_last = idx_first + lengthOfSubarray
            
            
            while idx_last <= length:
                subarray = tuple(arr[idx_first:idx_last])
                #print(f"current subarray is {subarray}")
                sum=0
                for element in subarray:
                    sum = sum + element
                #print(f"current sum is {sum}")
                #max_sum = sum
                
                if max_sum <= sum:
                    max_sum = sum
                #print(f"current max sum is {max_sum}")
                #sum_dict[subarray] = sum
                idx_first += 1
                idx_last = idx_first + lengthOfSubarray
                #print("=" * 50)
                
            lengthOfSubarray += 1

        '''best_subarray = max(sum_dict, key = sum_dict.get)
        max_sum = sum_dict[best_subarray]
        '''
        #print(f"max sum is {max_sum}")
        return(max_sum)
            
        
        
        

gang = Solution()
gang.maxSubarraySum([2,3,-8,7,-1,2,3])
        
        
        
class BetterSolution:
    def maxSubarraySum(self, arr):
        
        current_sum = 0
        max_sum = float('-inf')
        
        for i in range(len(arr)):
            current_sum = current_sum + arr[i]
            max_sum = max(current_sum, max_sum)
            
            if current_sum < 0:
                current_sum = 0
                
        return max_sum