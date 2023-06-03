from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            # some two numbers in the list equal to the target int
            # could loop through twice and check for equality of the ith and jth elements
            # that's probably the most basic way. Would that be O(n^2)? Probably. 

            # should we sort or filter the list?
            i=0
            j=1
            nums = list(filter(lambda x: (x < target), nums))
            while i < len(nums):
                while j < len(nums):
                    if nums[i] + nums[j] == target:
                        return [i, j]
                    j += 1
                i += 1
                j = i + 1


check = Solution()
print(check.twoSum([3, 2, 4], 6))