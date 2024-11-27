# Find the length of the longest consecutive elements sequence.

def longest_consecutive(nums):
    longest = 0
    seq = []
    for num in nums:
        if num-1 not in nums:
            length = 1
            
            while num + length in nums:
                length+=1
                seq.append(num)
            longest = max(length, longest)

    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive(nums))
