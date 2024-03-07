class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}

        for i in range(len(nums)):
            y = target - nums[i]
            if y in _dict:
                return [_dict[y], i]
            else:
                _dict[nums[i]] = i