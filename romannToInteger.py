# Challenge: Given a roman numeral convert it to an integer
# Constraints: 
  # 1 <= s.length <= 15
  # s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
  # It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        intOutput = 0

        # find instances where subtraction principle should be applied
        # apply subtraction principle
        # remove from the string roman numerals that were converted using the subtraction principle
        if 'IV' in s:
            intOutput += 4
            s = s.replace('IV','')
        if 'IX' in s:
            intOutput += 9
            s = s.replace('IX','')
        if 'XL' in s:
            intOutput += 40
            s = s.replace('XL','')
        if 'XC' in s:
            intOutput += 90
            s = s.replace('XC','')
        if 'CD' in s:
            intOutput += 400
            s = s.replace('CD','')
        if 'CM' in s:
            intOutput += 900
            s = s.replace('CM','')
        
        # convert remaining roman numerals to int
        for i in s:
            if i == 'I':
                intOutput += 1
            elif i == 'V':
                intOutput += 5
            elif i == 'X':
                intOutput += 10
            elif i == 'L':
                intOutput += 50
            elif i == 'C':
                intOutput += 100
            elif i == 'D':
                intOutput += 500
            elif i == 'M':
                intOutput += 1000
            
        return intOutput
Console
