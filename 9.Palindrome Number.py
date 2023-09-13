class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Converting the integer into string
        str_input = str(x)
        # reversing the str input
        rev_input = str_input[::-1]

        if str_input == rev_input:
            return True
        else:
            return False

''' EXPLANATION - 
This function converts the integer into string and in an another variable reverses out string and then it compares both of them. If our input is a palindrome then both the reversed and original will be same and it will print True otherwise False.'''
