import math
def bucketSort(arr):
    num_of_buckets = round(math.sqrt(len(arr)))
    max_val = max(arr)
    res = [] 
    for _ in range(num_of_buckets):
        res.append([])
    for j in arr:
        idx = math.ceil(num_of_buckets * j / max_val)
        res[idx - 1].append(j)
    for b in range(num_of_buckets):
        res[b].sort()
    k = 0
    for i in range(num_of_buckets):
        for j in range(len(res[i])):
            arr[k] = res[i][j]
            k += 1 

    return arr
    
arr = [5,9,3,1,2,8,4,7,6]
print (bucketSort(arr))

