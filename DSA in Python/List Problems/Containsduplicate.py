"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""

nums = [1, 2, 3, 1]
num_set = set(nums)
if len(nums) == len(num_set):
    print("false")
else:
    print("true")
