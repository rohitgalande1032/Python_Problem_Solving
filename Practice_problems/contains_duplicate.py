def contains_duplicate(nums):
    num_set = set(nums)

    l1 = len(nums)
    l2 = len(num_set)

    return l1 != l2

nums = [1, 2, 3, 4, 5, 5]
print("contains duplicates" if contains_duplicate(nums) else "No duplicate found")
