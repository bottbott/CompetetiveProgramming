class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate({ord(i): None for i in ',:\n\t.:;-?/<>!@#$%^&*()[]{} _`\\\"\''}).lower()
        reverse_str = list(s)
        reverse_str.reverse()
        reverse_str = ''.join(reverse_str)
        return s == reverse_str


sol = Solution()
print(sol.isPalindrome('abccba'))
print(sol.isPalindrome('A man, a plan, a canal: Panama'))
print(sol.isPalindrome("Marge, let's \"[went].\" I await {news} telegram."))