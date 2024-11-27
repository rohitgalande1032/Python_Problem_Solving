def product(nums):
    result = [0]*len(nums)

    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j: #Skip the current index
                product *= nums[j]
        result[i] = product

    return result

nums = [1, 2, 3, 4]
print(product(nums))