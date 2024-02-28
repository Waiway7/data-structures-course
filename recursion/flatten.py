def flatten(arr):
    lst = []
    for i in arr:
        if isinstance(i, list):
            lst += flatten(i)
        else:
            lst.append(i)
    return lst

print (flatten([[1], [2], [3]]))