class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        output = []
        
        value_list = []
        sorted_i = ""
        sorted_c = ""
        
        i_index = 0
        c_index = 0
        i=0
        c=0
        
        while i_index < len(strs):
            i =strs[i_index]
            
            #print(f"here is i: {i}")
            
            value_list = []
            sorted_i = sorted(i)
            value_list.append(i)
            
            #print(f"here is value_list: {value_list}")
            
            strs.remove(i)
            
            #print(f"here is strs: {strs}")
            
            while c_index < len(strs):
                c = strs[c_index]
                
                #print(f"NOW here is c: {c}")
                #print(f"NOW here is new length: {len(strs)}")
                
                sorted_c = sorted(c)
                if sorted_c == sorted_i:
                    value_list.append(c)
                    
                    #print("repeat anagram found. value_list has been updated")
                    #print(f"NOW here is value_list: {value_list}")
                    
                    strs.remove(c)
                    
                    #print(f"NOW here is new length: {len(strs)}")
                    #print(f"NOW here is strs: {strs}")
                    
                    #c_index+=1
                else:
                    
                    c_index+=1
                #print("=" *10)
            #i_index+=
            c_index = 0
            #print("=" *50)
            output.append(value_list)
                    
            
            
        return output
    
strs = ["act","pots","tops","cat","stop","hat"]
        
gang = Solution()
print(gang.groupAnagrams(strs))   