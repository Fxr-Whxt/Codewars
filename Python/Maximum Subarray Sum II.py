'''Take a look to the kata Maximum Subarray Sum https://www.codewars.com/kata/maximum-subarray-sum In that kata (if you solved it), you had to give the maximum value of the elements of all the subarrays.

In this kata, we have a similar task but you have to find the sub-array or sub-arrays having this maximum value for their corresponding sums of elements. Let's see some examples:

[-2, 1, -3, 4, -1, 2, 1, -5, 4] returns [[4, -1, 2, 1], 6]

If in the solution we have two or more arrays having the maximum sum value, the result will have an array of arrays in the corresponding order of the array, from left to right.

[4, -1, 2, 1, -40, 1, 2, -1, 4]) returns [[[4, -1, 2, 1], [1, 2, -1, 4]], 6]  # From left to right [4, -1, 2, 1] appears in the array before than [1, 2, -1, 4].

If the array does not have any sub-array with a positive sum of its terms, the function will return [[], 0].

See more cases in the Example Test Cases Window. Enjoy it!'''



def find_subarr_maxsum(arr):
    subarrs = [arr[i:j+1] for i in range(len(arr)) for j in range(i, len(arr))]

    maxsum = max((sum(subarr) for subarr in subarrs))
    if maxsum < 0:
        return [[], 0]
    maxes = [subarr for subarr in subarrs if sum(subarr) == maxsum]
    if len(maxes) == 1:
        maxes = maxes[0]

    return [maxes, maxsum]