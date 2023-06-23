from typing import List

class Solution1:
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

class Solution2:
    def binarySearch(self, nums, key, start, end):
        middle = (end + start) // 2
        print(f'start: {start}, {nums[start]}. middle: {middle}, {nums[middle]}. end: {end}, {nums[end]}')
        if (start > end):
             return None
        elif (nums[middle] == key):
              return middle
        elif (nums[middle] > key):
            return self.binarySearch(nums, key, start, middle - 1)
        else:
            return self.binarySearch(nums, key, middle+1, end)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # I think we can improve this by sorting the list. O(nlogn)
        # Then iterating through the list O(n)
        # And doing a binary search for target - currentIndex O(logn)
        nums_sorted = sorted(nums)
        found = False
        num1 = None
        num2 = None
        for index1, num in enumerate(nums_sorted):
            # can't use 'x in s': it works in O(n) and we need O(logn)
              print(f'Searching for {target - num} in {nums_sorted}.')
              index2 = self.binarySearch(nums_sorted, target - num, 0, len(nums_sorted) - 1)
              if (index2 is not None and index1 != index2):
                   found = True
                   num1 = nums_sorted[index1]
                   num2 = nums_sorted[index2]
                   break
        if (found == True):
             if (num1 == num2):
                # if the numbers are the same then we need to skip past the first found index
                return [nums.index(num1), nums.index(num2, nums.index(num1) + 1)]
             else:
                return [nums.index(num1), nums.index(num2)]
        return None
        
class Solution3:
    # NeetCode Solution
    # We can use a HashMap to do our equality checks in constant time. 
    # This takes O(n) memory because of the hashmap whereas the other solutions were O(1) for memory.
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         checked = {} # make an empty dict/hashmap
         for index, num in enumerate(nums): # loop over all numbers in the input
              key = target - num # what we are actually interested in finding a match of. 
              if (key in checked):
                   return [index, checked[key]]
              else: # we slowly build up the hashmap
                   print(f'num: {num}. index: {index}')
                   checked.update({num: index})
         return None
    

check = Solution3()
print(check.twoSum([2,5,5,11], 7))