#SOLVED ALL BY MYSELF
#Leetcode Easy :(

class Solution:
    def romanToInt(self, s: str) -> int:
        operators = "IXC"
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        sum = 0
        next_letter = "I"
        i = 0
        
        while i < len(s):
            if i == len(s) -1:
                sum = sum + dict[s[i]]
                return sum
            else:
                next_letter = s[i+1]
                if s[i] in operators and dict[next_letter] > dict[s[i]]:
                    next_letter = s[i+1]
                    sum = sum + (dict[next_letter] - dict[s[i]])
                    i = i + 2
                else:
                    sum = sum + dict[s[i]]
                    i+=1
        
        return sum
            
                    
gang = Solution()
print(gang.romanToInt("MMVIII"))
            