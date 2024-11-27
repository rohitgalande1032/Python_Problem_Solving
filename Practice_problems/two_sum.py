# Find two numbers in an array that add up to a specific target. Return their indices.

# Brute Force Approach
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and nums[i]+nums[j] == target:
                return [i, j]

# Optimal approach

# def two_sum(nums, target):
#     num_set = {}
#     for i, num in enumerate(nums):
#         complement = target-num
#         if complement in num_set:
#             return [num_set[complement], i]
#         num_set[num] = i

nums = [2, 11, 15, 7]
target = 9
print(two_sum(nums, target))