# Every element in the array appears twice except for one. Find that single one.

# def find_single(nums):
#     num_count = {}
#     for num in nums:
#         if num in num_count:
#             num_count[num] += 1
#         num_count[num]=1

#     for element, count in num_count.items():
#         if count < 2:
#             return element
        
def find_single(nums):
    for num in nums:
        if nums.count(num) < 2:
            return num
    return -1


nums = [4, 1, 2, 1, 2]  
single = find_single((nums))  
print(f"{single} is single element")   