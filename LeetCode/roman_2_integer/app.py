class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        double_numerals = {
            'CM': 900,
            'CD': 400,
            'XC': 90,
            'XL': 40,
            'IX': 9,
            'IV': 4
        }
        roman_numerals = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }
        step = 0
        while step < len(s):
            char = s[step]
            if step == len(s) - 1:
                total += roman_numerals[char]
                break
            next_char = s[step+1]
            if char + next_char in double_numerals:
                total += double_numerals[char+next_char]
                step += 2
            else:
                total += roman_numerals[char]
                step += 1
        return total

app = Solution()
print(app.romanToInt('III'))
print(app.romanToInt('LVIII'))
print(app.romanToInt('MCMXCIV'))
print(app.romanToInt('IX'))