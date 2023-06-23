class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        ##
        ## Should run in O(n) since we are only ever looping over either of the strings. 
        ## More specifically O(s + t)
        ##
        if len(s) != len(t): # can't have anagrams with unequal length words
            return False
        if len(s) == 0 and len(t) == 0: # anagram of zero length. vacously true.
            return True

        # initialize dictionaries with each letter as a key and the value as 0 for a counter. 
        dicta = {letter:0 for letter in [chr(a) for a in range(97, 123)]} 
        dictb = {letter:0 for letter in [chr(a) for a in range(97, 123)]}
        
        for letter in s:
            dicta[letter] += 1

        for letter in t:
            dictb[letter] += 1
        
        return dicta == dictb
    
from collections import Counter
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        # Counter is a special Python data structure that is designed for counting hashable objects. 
        return Counter(s) == Counter(t)
    
# write a solution that uses constant memory (not extra dictionaries)
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # can't have anagrams with unequal length words
            return False
        if len(s) == 0 and len(t) == 0: # anagram of zero length. vacously true.
            return True

        return list(s).sort() == list(t).sort()

test = Solution1()

print(test.isAnagram('barf', 'farb'))
print(test.isAnagram('barf', 'farbf'))
print(test.isAnagram('', ''))