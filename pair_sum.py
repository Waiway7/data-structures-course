def twoSum(self, nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i in range(len(nums)):
        r = target - nums[i]
        if nums[i] in num_map:
            return [i, num_map[nums[i]]]
        num_map[r] = i