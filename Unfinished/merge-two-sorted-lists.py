def mergeTwoLists(list1, list2):
    sorted_list = list1 + list2
    sorted_list.sort()
    return sorted_list

solution = mergeTwoLists([1,2,4], [1,3,4])
print(solution)
