class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # can't have anagrams with unequal length words
            return False
        if len(s) and len(t) == 0: # anagram of zero length. vacously true.
            return True

        dicta = {letter:0 for letter in [chr(a) for a in range(97, 123)]} 
        dictb = {letter:0 for letter in [chr(a) for a in range(97, 123)]}
        
        for letter in s:
            dicta[letter] += 1

        for letter in t:
            dictb[letter] += 1
        
        return dicta == dictb

test = Solution()

print(test.isAnagram('barf', 'farb'))
print(test.isAnagram('barf', 'farbf'))
print(test.isAnagram('', ''))