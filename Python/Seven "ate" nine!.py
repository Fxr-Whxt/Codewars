'''Seven is a hungry number and its favourite food is number 9. 
Whenever it spots 9 through the hoops of 8, it eats it! Well, not anymore, 
because you are going to help the 9 by locating that particular sequence (7,8,9) in an array of 
digits and tell 7 to come after 9 instead. Seven "ate" nine, 
no more! (If 9 is not in danger, just return the same array)'''

def hungry_seven(arr):
    i = 0
    while i < len(arr) - 2:
        if arr[i] == 7 and arr[i+1] == 8 and arr[i+2] == 9:
            arr[i:i+3] = [8, 9, 7]
            if i > 0:
                i -= 1
        else:
            i += 1
    return arr