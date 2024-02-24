def maxProduct(self, nums: List[int]) -> int:
    
    num_max = 0
    num_second = 0
    for i in nums:
        if i > num_max:
            num_second = num_max
            num_max = i
        else:
            num_second = max(num_second, i)
    return (num_max - 1) * (num_second - 1)