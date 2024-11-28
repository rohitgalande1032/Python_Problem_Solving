# def rotate_array(nums, k):
#     n = len(nums)

#     def reverse_array(start, end):
#         while start < end:
#             nums[start], nums[end] = nums[end], nums[start]
#             start+=1
#             end-=1

#     reverse_array(0, n-1)
#     reverse_array(0, k-1)
#     reverse_array(k, n-1)
#     return nums


def rotate_array(nums, k):
    n = len(nums)
    temp = [0]*n

    for i in range(n):
        temp[(i+k) % n] = nums[i]
    return temp
#Saperate function to reverse

# def reverse_arr(nums):
#     n = len(nums)
#     start = 0
#     end = n-1
#     while start < end:
#         nums[start], nums[end] = nums[end], nums[start]
#         start+=1
#         end-=1

#     return nums


def first_char(s):
    dic = {}

    for ch in s:
        if ch in dic:
            dic[ch] +=1
        else:
            dic[ch] = 1

    for ele, count in dic.items():
        if count == 1:
            return ele

nums = [1, 2, 3, 4, 5, 6, 7]
# num2 = [1, 2, 3, 4, 5, 6, 7 ]
k=3
print(rotate_array(nums, k))
# print(reverse_arr(num2))
string = "swiwss"
print(first_char(string))