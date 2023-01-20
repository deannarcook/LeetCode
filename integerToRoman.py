"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:
Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Example 2:
Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 3:
Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= num <= 3999
"""

class Solution(object):

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        num = num

        # Create variable that will be returned by function
        roman = ''

        # Create dictionary storing integer values and their corresponding roman numeral
        intRomanDictionary= {1000:'M',900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X',
                             9: 'IX', 5:'V', 4:'IV',  1:'I'}

        # Iterate through dictionary keys
        for key in intRomanDictionary:
            # Assign the value associated with the key to a variable called romanNumeral
            currentRomanNumeral = intRomanDictionary[key]
            # Check if the user provided number is divisible by the key
            if num/key >= 1:
                # Cast the value to an int and store in variable
                romanNumeralOccurances = int(num/key)
                # Multiple the current roman numeral by the number of times the roman numeral will appear in the
                # final output. Then concatenate the result to the roman variable.
                roman += currentRomanNumeral * romanNumeralOccurances
                # Decrement num
                num -= romanNumeralOccurances * key

        return roman

# create object of Solution class
solution = Solution()

# call intToRoman function
print(solution.intToRoman(num = 1994))

"""
Below is an alternative solution that utilizes lists instead of a dictionary. The dictionary solution is better 
because it requires 1) less code to accomplish the same outcome and 2) is a better fit for the key:value relationship 
between an integer and it's corresponding roman numeral
        romanList = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        integerList = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

        i = 0

        for integer in integerList:
            romanNumeral = romanList[i]
            if num / integer >= 1:
                M = int(num / integer)
                roman += romanNumeral * M
                num -= M * integer
            i += 1 
"""