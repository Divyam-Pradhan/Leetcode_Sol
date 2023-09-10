# SOLUTIONT OF LEETCODE PROBLEM - TWO SUM II- Input array in Sorted (MEDIUM)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers)-1
        while i < j:
            var = numbers[i] + numbers[j]
            if target == var:
                return [i+1,j+1]
            elif var < target:
                i +=1
            else:
                j -=1

''' EXPLANATION OF CODE - 
Let's say we have a sorted list of numbers: [2, 7, 11, 15, 17] and our target is target = 9. We want to find two numbers in this list that add up to the target.

Here's how the code works step by step:

Initialize two pointers, i and j, one at the beginning (i.e., 0) and one at the end (i.e., the last index) of the list. In this case, i is at index 0, and j is at index 4 (since the list has 5 elements).

Enter a while loop that continues as long as i is less than j. This loop will keep narrowing down the search.

Calculate the sum of the numbers at positions i and j: var = numbers[i] + numbers[j]. In this case, var = 2 + 17 = 19.

Check if var is equal to the target (target = 9). It's not equal (19 is greater than 9), so we move to the next step.

Since var is greater than the target, we need to reduce the sum. To do this, we move the j pointer one step to the left by decrementing j by 1. Now, j is at index 3.

Calculate the sum again: var = numbers[i] + numbers[j]. Now, var = 2 + 15 = 17.

Check if var is equal to the target (target = 9). It's still not equal (17 is greater than 9), so we move the j pointer again.

We keep repeating steps 5-7 until we find two numbers whose sum equals the target or until i becomes greater than or equal to j. In this case, we continue reducing j.

Eventually, var becomes equal to the target: var = 7 + 2 = 9.

We found two numbers (7 and 2) that add up to the target (9), so we return their indices plus 1 (since the problem assumes 1-based indexing). In this case, we return [2, 1], which means the number at index 2 (7) and the number at index 1 (2) add up to 9.
'''
