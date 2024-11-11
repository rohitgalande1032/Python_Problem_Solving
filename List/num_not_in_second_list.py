# Given Two Lists—1, 2, 3, 4, 5 and 2, 3, 1, 10, 5—Can You Find Which Number Is Not Present in the Second Array?
def checkNumNotInSecondList(l1, l2):
    num = set()
    for item in l1:
        if item not in l2:
            num.add(item)
    return num

if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5, 10]
    l2 = [2, 3, 1, 0, 5]

    print(checkNumNotInSecondList(l1, l2))
