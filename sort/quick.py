def partition(arr, low, high):
    pivot = arr[high]
    idx = low - 1

    for i in range(low, high):
        if arr[i] <= pivot:
            idx += 1
            arr[i], arr[idx] = arr[idx], arr[i]

    arr[idx + 1], arr[high] = arr[high], arr[idx + 1]
    return idx + 1

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
arr = [10, 7, 8, 9, 1, 5]
quickSort(arr, 0, len(arr) - 1)
print (arr)