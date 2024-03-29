class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]   
        value =  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        num = 0
        i = 0
        while s != '':
            while s.startswith(symbol[i]):
                num += value[i]
                s = s[len(symbol[i]):]
            i += 1
        return num
    
