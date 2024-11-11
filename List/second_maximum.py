
def secondMax(lis):
    # Initialize first and second with very low values
    first = 0
    second = 0

    for num in lis:
        if num > first:
            second = first   # update second first
            first = num
        elif num > second and num != first:
            second = num
    return second

if __name__ == "__main__":
    lis = [1, 4, 3, 5, 9, 10, 8, 2, 12]
    print(f"Second max is {secondMax(lis)}")
