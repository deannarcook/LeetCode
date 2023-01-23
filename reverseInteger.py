"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        inputAsString = str(x)
        isNegative = False

        # if input is negative
        if inputAsString[0] == '-':
            print('input is negative')
            reverseList = inputAsString.replace('-', '')[::-1]
            isNegative = True
        else:
            print('input is not negative')
            print(inputAsString)
            reverseList = inputAsString[::-1]

        # turn reversedList into string
        returnString = ''
        for i in reverseList:
            returnString += i

        # if inputString is negative make return value negative
        if isNegative == True:
            returnString = int(returnString.rstrip('0')) * -1
        else:
            returnString = int(returnString.rstrip('0'))

        # check if return string is not a 32 bit int
        if returnString >= -(2 ** 31) and returnString <= (2 ** 31 - 1):
            return returnString
        else:
            return 0

objectSolution = Solution()

print(objectSolution.reverse(90100))

