def capitalizeFirst(arr):
    
    if len(arr) == 0:
        return []
    
    return [arr[0].title()] + capitalizeFirst(arr[1:])