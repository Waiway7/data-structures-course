def bubbleSort(arr):
    for x in range(len(arr)):
        for y in range(x + 1, len(arr)):
            if arr[x] > arr[y]:
                arr[x], arr[y] = arr[y], arr[x]
            else:
                continue
    return arr
arr = [5,9,3,1,2,8,4,7,6]
print (bubbleSort(arr))