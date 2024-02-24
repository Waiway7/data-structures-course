def check_same_frequency(list1, list2):
    # TODO
    if len(list1) != len(list2):
        return False
    dict1 = {}
    for i in range(len(list1)):
        if list1[i] in dict1:
            dict1[list1[i]] += 1
        else:
            dict1[list1[i]] = 1
        if list2[i] in dict1:
            dict1[list2[i]] -= 1
        else:
            dict1[list2[i]] = 1
    
    for i in dict1.values():
        if i != 0:
            return False
    return True