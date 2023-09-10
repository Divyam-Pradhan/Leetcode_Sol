# LEETCODE - 2SUM Problem in Python 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref_dict = {}
        for i,num in enumerate(nums):
            diff = target - nums[i]

            if diff in ref_dict:
                return [i, ref_dict[diff]]
            else:
                ref_dict[num] = i

''' Explanation of this code - 
Line 5 - > Created an empty dictionary 
Line 6 -> Created a key value relation of elements of List Nums using enumerate function
Line 7 - > Calculating the difference between the first element and th target element
Line 9-10 -> Checking if the difference calculated in above step exists in the dictionary we created ( iF IT EXISTS THEN RETURN THEIR INDICES AS SOLUTION )
Line 11-12 -> If the difference doesn't exists then add the element with which we have calculated into the dictionary for reference in future computation . 

Example Working - 

nums = [2, 7, 11, 15]
target = 9

The code enters a loop to iterate through the nums array:

Iteration 1: i = 0, value = 2

Calculate remaining = target - nums[i] = 9 - 2 = 7.

Check if remaining (7) is in seen. It's not present yet.

Add value (2) to the seen dictionary with its index i (0): seen = {2: 0}.

Iteration 2: i = 1, value = 7

Calculate remaining = target - nums[i] = 9 - 7 = 2.

Check if remaining (2) is in seen. It is present with an index of 0.

You've found a pair of numbers (2 and 7) whose sum equals the target (9). Return [1, 0] because 2 is at index 1, and 7 is at index 0 in the nums array.'''
