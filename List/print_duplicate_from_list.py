def print_dup(lst):
    dup_list = []
    for item in lst:
        if lst.count(item) > 1 and item not in dup_list:
            dup_list.append(item)
    return dup_list

def print_dup_dict(lst):
    dup_list = []
    item_count = {}

    for item in lst:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

    for element, count in item_count.items():
        if count > 1 and element not in dup_list:
            dup_list.append(element)
    return dup_list



if __name__ == "__main__":
    lst = [1, 3, 5, 7, 7, 5, 4, 3, 8, 9, 8]
    print(print_dup(lst))

    print(print_dup_dict(lst))
    