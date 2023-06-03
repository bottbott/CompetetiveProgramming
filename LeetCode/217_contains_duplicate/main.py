from typing import List

# solution from leetcode. 
class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sets have no duplicate elements, so convert to set and compare to original
        # list
        return nums != list(set(nums))

# First solution.
# Time complexity: O(n) since we may need to go over every element in the list
# Space complexity: O(n) since we may add every item in the list to our new dict. 
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        compare_checker = {} # empty dict
        for num in nums: # iterate over all numbers
            if num not in compare_checker: # if the number isn't in the dict
                compare_checker[num] = 0 # set a key of num to 0. ## wou
            else:
                return True
        return False
    
## since the value isn't really required. i'm going to refactor my solution to use sets
## After submitting to LeetCode. This was slower and used more memory than the previous solution.
## space/time same as above. 
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        compare_checker = set()
        for num in nums:
            if num not in compare_checker: # this is a fast check (O(1)) rather than O(n)
                compare_checker.add(num)
            else:
                return True
        return False

sol = Solution()
print(sol.containsDuplicate([1,1]))
print(sol.containsDuplicate([1,2]))
