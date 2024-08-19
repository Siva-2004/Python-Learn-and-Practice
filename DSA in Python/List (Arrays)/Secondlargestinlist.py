"""
Find the second largest element in the list.

time complexity = O(n)
"""

arr = [2, 231, 14, 524, 2354, 231, 523, 12, 3512, 5, 1245]
first_max = 0
second_max = -1
for i in arr:
    if i > first_max:
        first_max = i

for i in arr:
    if i > second_max and i < first_max:
        second_max = i

print(second_max)
