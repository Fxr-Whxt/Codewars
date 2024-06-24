'''Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'

'''


def solution(string):
     str1 = ''
     for i in range(len(string)-1,-1,-1):
        str1 += string[i]
     return str1
