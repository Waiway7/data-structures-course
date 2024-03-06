def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        return merge(arr, l, m, r)

def merge(arr, l, m, r):
    len_l_sub_arr = m - l + 1
    len_r_sub_arr = r - m

    l_sub_arr = [ arr[l + i] for i in range(0, len_l_sub_arr)]
    r_sub_arr = [ arr[m + 1 + i] for i in range(0, len_r_sub_arr)]

    i = 0
    j = 0 
    k = l

    while i < len_l_sub_arr and j < len_r_sub_arr:
        if l_sub_arr <= r_sub_arr:
            arr[k] = l_sub_arr[i] 
            i += 1
        else:
            arr[k] = r_sub_arr[j]
            j += 1
        k += 1
    
    while i < len_l_sub_arr:
        arr[k] = l_sub_arr[i]
        i += 1
        k += 1
    while j < len_r_sub_arr:
        arr[k] = r_sub_arr[j]
        j += 1
        k += 1 
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print (mergeSort(arr, 0, n - 1))
