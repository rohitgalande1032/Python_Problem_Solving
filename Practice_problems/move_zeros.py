# Move all 0s to the end of an array while maintaining the relative order of the non-zero elements.

# def move_zeros(nums):
#     for num in nums:
#         if num == 0:
#             nums.remove(num)
#             nums.append(0)
#     return nums


def move_zeros(nums):
    pos = 0 # Position to place the next non-zero
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[pos] = nums[pos], nums[i]
            pos+=1
    return nums

nums = [0, 1, 0, 3, 12]
print(move_zeros(nums))