# def find_duplicates(nums):
#     dup_list = []
#     num_count = {}

#     for num in nums:
#         if num in num_count:
#             num_count[num] += 1
#         else:
#             num_count[num] = 1

#     for element, count in num_count.items():
#         if count > 1:
#             dup_list.append(element)
    
#     return dup_list

def find_duplicates(nums):
    dup_list = []
    for num in nums:
        if nums.count(num) > 1 and num not in dup_list:
            dup_list.append(num)

    return dup_list

nums = [1, 2, 4, 5, 4, 2, 7 ,5]
print(find_duplicates(nums))