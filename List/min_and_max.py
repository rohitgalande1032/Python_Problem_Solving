def min_max(lst):
    min = lst[0]
    max = lst[0]

    for num in lst:
        if num < min:
            min = num
        elif num > max:
            max = num
    return min, max


if __name__ == "__main__":
    lst = [3, 5, 44, 65, 78, 56, 45, 2, 10]
    print(min_max(lst))