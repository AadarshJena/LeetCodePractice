class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_split =[]
        t_split = []
        
        for s_letter in s:
            s_split.append(s_letter)
           
        for t_letter in t:
            t_split.append(t_letter)
        
        
        s_sorted = sorted(s_split)
        t_sorted = sorted(t_split)
        
        #print(f"here is s_sorted: {s_sorted}")
        #print(f"here is t_sorted: {t_sorted}")
        
        if s_sorted == t_sorted:
            return True
        else:
            return False
        
        
