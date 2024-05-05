'''task: Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals:

    1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
    2008 is written as 2000=MM, 8=VIII; or MMVIII
    1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examplies:
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
  86 -> "LXXXVI"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1
'''




class RomanNumerals:
    
    sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    @staticmethod
    def to_roman(number):
        i = ''
        point = 0
        while number:
            x = number // RomanNumerals.num[point]
            number %= RomanNumerals.num[point]
            
            while x:
                i += RomanNumerals.sym[point]
                x -= 1
            point += 1
        return i

    @staticmethod
    def from_roman(num):
        i = 0
        for id, val in enumerate(num):
            first = RomanNumerals.num[RomanNumerals.sym.index(val)]
            second = RomanNumerals.num[RomanNumerals.sym.index(num[id + 1])] if id + 1 != len(
                num) else -1
            if first >= second:
                i += first
            else:
                i -= first
        return i