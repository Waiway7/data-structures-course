def productOfArray(arr):
    if (len(arr) == 0):
        return 0
    elif len(arr) == 1:
        return arr[0]
    return arr.pop() * productOfArray(arr)