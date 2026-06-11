class Solution:
    def reverseArray(self, list1):
        # code here
        length = len(list1)
        temp = 0
        lower_idx=0
        upper_idx = length -1
        
        while lower_idx < upper_idx:
            temp = list1[lower_idx]
            list1[lower_idx] = list1[upper_idx]
            list1[upper_idx] = temp
            lower_idx +=1
            upper_idx = upper_idx-1
        return list1
    
    
#Array Reverse on Geeks for Geeks