def remove_dup_set(lst):
    return list(set(lst))

def remove_dup_loop(lst):
    unique_list = []

    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


if __name__ == "__main__":
    lst = [1, 2, 4, 5, 6, 6, 5, 4, 8, 7]
    #using set
    print(remove_dup_set(lst))
    #using loop
    print(remove_dup_loop(lst))