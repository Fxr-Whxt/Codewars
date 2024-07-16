'''This kata is the performance version of Don't give me five by user5036852.

Your mission, should you accept it, is to return the count of all integers in a given range which do not contain the digit 5 (in base 10 representation).
You are given the start and the end of the integer range. The start and the end are both inclusive.

Examples:

1,9 -> 1,2,3,4,6,7,8,9 -> return 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> return 12

The result may contain fives. ;-)
The start will always be smaller than the end. Both numbers can be also negative.

The regions can be very large and there will be a large number of test cases. So brute force solutions will certainly time out!

Good luck, warrior!
'''



def dont_give_me_five(start, end):
    COUNTS = {1: 9, 2: 81, 3: 729, 4: 6561, 5: 59049, 6: 531441, 7: 4782969, 8: 43046721, 9: 387420489, 10: 3486784401, 11: 31381059609, 12: 282429536481, 13: 2541865828329, 14: 22876792454961, 15: 205891132094649, 16: 1853020188851841, 17: 16677181699666569, 18: 150094635296999121, 19: 1350851717672992089, 20: 12157665459056928801}
    if start < 0 and end < 0:
        start, end = abs(end), abs(start)
    ss = start
    if start > 0:
        start -= 1
    def count_not_fives(num):
        num = abs(num)
        if num < 5:
            return num
        elif num == 5:
            return 4
        elif num < 10:
            return num - 1
        num = str(num)
        significance = len(num) - 1
        sequence_length = 0
        
        for i in range(len(num) - 1):
            digit = int(num[i])
            if digit < 5:
                sequence_length += digit * COUNTS[significance]
            elif digit == 5:
                sequence_length += digit * COUNTS[significance] - 1
                
                return sequence_length
            else:
                sequence_length += COUNTS[significance + 1]
                sequence_length -= (10 - digit) * COUNTS[significance]

            significance -= 1

        
        sequence_length += count_not_fives(int(num[-1]))
        return sequence_length
    
    
    start_sequence = count_not_fives(start)
    end_sequence = count_not_fives(end)
    
    if ss <= 0:
        return end_sequence + start_sequence + 1
    return end_sequence - start_sequence