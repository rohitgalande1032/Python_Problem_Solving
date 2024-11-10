def duplicates(lst):
    dup_list = []
    for element in lst:
        if lst.count(element)>1 and element not in dup_list:
            dup_list.append(element)
    return dup_list

def duplicate_dict(lst):
    dic = {}
    dup_list = []
    for element in lst:
        if element in dic:
            dic[element] += 1
        else:
            dic[element] = 1
    
    for element, count in dic.items():
        if count > 1:
            dup_list.append(element)
    return dup_list



if __name__ == "__main__":
    lst = [1, 5, 3, 6, 8, 3, 5, 8, 9, 12]

    #Print list
    print(lst)
    #Find length
    print(len(lst))
    #print minimum
    print(min(lst))
    #return maximum
    print(max(lst))
    #access list elements
    print(lst[2])
    print(lst[1:4])
     #add at last
    lst.append(20)
    #remove element at specified index
    lst.pop(3)
    #lst.extend(lst) //add all elements of lst at end

    #remove element with specifies value
    lst.remove(20)
    
    #lst.clear()  --> remove all lst
    
    #reverse list
    #lst.reverse()

    #sort the list
    #lst.sort()

    #update list
    lst[2] = 9
    print(lst)

   

    #Print duplicate elements using list.count(element)
    print(duplicates(lst))

    #Print duplicate elements using dictionary
    dup_list = duplicate_dict(lst)
    print(dup_list)

   




