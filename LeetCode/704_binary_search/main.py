from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # okay.
        # binary search is all about looking in smaller version of the
        # original list by slicing the list or moving list index pointer
        # around. this particular one is set up for solution by recursion.

        # base case
        # not in the list
        if len(nums) == 0:
            return -1
        
        middle = len(nums) // 2
        index = 0

        # base case
        # target is the only one in the list
        if len(nums) == 1 and nums[0] == target:
            return middle

        if target < nums[middle]:
            index -= middle
            self.search(nums[0:middle], target)
        elif target == nums[middle]:
            return middle
        elif target > nums[middle]:
            index += middle
            self.search(nums[middle:], target)
        
        return middle

sol = Solution()
list_ = [-1,0,3,5,9,12]
print(sol.search(list_, -1))
print(sol.search(list_, 0))
print(sol.search(list_, 3))
print(sol.search(list_, 5))
print(sol.search(list_, 9))