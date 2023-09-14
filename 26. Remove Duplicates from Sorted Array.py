class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    i = 0

    for num in nums:
      if i < 1 or num > nums[i - 1]:
        nums[i] = num
        i += 1

    return i


'''explanation - 
The code starts by initializing a variable i to 0. This i will be used to keep track of the position where unique elements should be stored in the nums list.

It then goes through each number (num) in the nums list one by one.

For each num, it checks two conditions:

If i is less than 1 (meaning it's at the beginning of the list) or
If the current num is greater than the previous unique number (the one at nums[i - 1]).
If either of these conditions is met, it means that num is a unique element.

In that case, it updates the nums list at the position i with the current num, effectively storing the unique element.

After storing the unique element, it increments i to prepare for the next unique element.

This process continues until all elements in the nums list have been checked.

Finally, it returns the value of i, which represents the number of unique elements found in the list.'''
