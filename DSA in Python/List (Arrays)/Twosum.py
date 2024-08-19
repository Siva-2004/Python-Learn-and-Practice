"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

nums = [2, 7, 13, 15]
target = 9

hashmap = {}
for i in range(len(nums)):
    diff = target - nums[i]
    if diff in hashmap:
        print([hashmap[diff], i])
    else:
        hashmap[nums[i]] = i
