#In an Array Where the Numbers 1–10 Are Stored, and One Number Is Missing, How Do You Find It?

# Algorithm: 

# Calculate the sum of the first n natural numbers as sumtotal= n*(n+1)/2.
# Create a variable sum to store the sum of array elements.
# Traverse the array from start to end.
# Update the value of sum as sum = sum + array[i].
# Print the missing number as the sum total - sum.

def missingNumber(lst):
    n = 10
    sum_total = n*(n+1)//2
    sum = 0
    for num in lst:
        sum += num
    return sum_total - sum


if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    print(missingNumber(lst))
    