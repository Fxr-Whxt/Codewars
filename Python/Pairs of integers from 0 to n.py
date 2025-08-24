'''Write a function that accepts an integer argument n and generates an array containing the pairs of integers [a, b] that satisfy the condition

0 <= a <= b <= n

The pairs should be sorted by increasing values of a, then by increasing values of b.

For example,

for input: 2
it should return: [  [0, 0], [0, 1], [0, 2],  [1, 1], [1, 2],  [2, 2]  ]

'''


def generate_pairs(n):
    pairs = []
    for a in range(n + 1):  # Loop from 0 to n (inclusive)
        for b in range(a, n + 1):  # Loop from 'a' to n (inclusive)
            pairs.append([a, b])
    return pairs