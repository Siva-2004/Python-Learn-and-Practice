"""
Find the maximum value in a given list.
time conplexity : O(n)

"""

arr = [2, 231, 14, 524, 2354, 231, 523, 12, 3512, 5, 1245]
max = 0
for num in arr:
    if num > max:
        max = num

print(max)
