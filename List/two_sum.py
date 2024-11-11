def single_pair(lst, target):
    for num in lst:
        complement = target - num
        if complement in lst:
            return complement, num


def all_pairs(lst, target):
    seen = set()
    pairs = []

    for num in lst:
        complement = target-num
        if complement in seen: #If complement exists in seen, then num and complement form a valid pair that adds up to target_sum.
            pairs.append((complement, num))
        seen.add(num) #Add num to the seen set. This ensures that the element is available for future complement checks.
    return pairs


if __name__ == "__main__":
    lst = [4, 3, 5, 2, 6, 1, 7, 9, 8]
    target = 7
    print(single_pair(lst, target))

    print(f"All pair of {target} = {all_pairs(lst, target)}")

