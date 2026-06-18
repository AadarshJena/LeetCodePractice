class Solution:
    def intToRoman(self, num: int) -> str:
        
        string = str(num)
        
        
        onesExceptions = {4: "IV", 9: "IX"}
        tensExceptions = {4: "XL", 9: "XC"}
        hundredsExceptions = {4: "CD", 9: "CM"}
        
        
        
        thousands = ""
        hundreds = ""
        tens = ""
        ones = ""
        
        place = 0
        i = len(string) - 1
                
                
        while i > -1:
            current_digit = int(string[i])
            if place == 0:
                if onesExceptions.get(current_digit, 0) != 0:
                    ones += onesExceptions[current_digit]
                    i = i - 1
                    place +=1
                    
                elif current_digit > 5:
                    ones += ("V" + ( "I" * (current_digit %5)))
                    i = i - 1
                    place +=1
                elif current_digit == 5:
                    ones += "V"   
                    i = i - 1
                    place +=1 
                else:
                    ones  += ("I" * current_digit)
                    i = i - 1
                    place +=1        
            elif place == 1:
                if tensExceptions.get(current_digit, 0) != 0:
                    tens += tensExceptions[current_digit]
                    i = i - 1
                    place +=1
                    
                elif current_digit > 5:
                    tens += ("L" + ( "X" * (current_digit %5)))
                    i = i - 1
                    place +=1
                elif current_digit == 5:
                    tens += "L"   
                    i = i - 1
                    place +=1                    
                else:
                    tens  += ("X" * current_digit)
                    i = i - 1
                    place +=1
            elif place == 2:
                if hundredsExceptions.get(current_digit, 0) != 0:
                    hundreds += hundredsExceptions[current_digit]
                    i = i - 1
                    place +=1
                    
                elif current_digit > 5:
                    hundreds += ("D" + ( "C" * (current_digit %5)))
                    i = i - 1
                    place +=1
                elif current_digit == 5:
                    hundreds += "D"   
                    i = i - 1
                    place +=1    
                else:
                    hundreds  += ("C" * current_digit)
                    i = i - 1
                    place +=1
            elif place == 3:
                thousands += ("M" * current_digit)
                i = i-1
                place += 1
            else:
                break
        
        return (thousands + hundreds + tens + ones)
                
                
            
        
    def betterIntToRoman(self, num: int) -> str:
        values  = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = ""
        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]
        return result


gang = Solution()
print(gang.intToRoman(1994))
print(gang.betterIntToRoman(1994))
            
            

