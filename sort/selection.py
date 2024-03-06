def selection(arr):
    
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

arr = [5,9,3,1,2,8,4,7,6]
print (selection(arr))

