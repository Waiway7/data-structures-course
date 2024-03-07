class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        0 = 24
        1 = 1 * 12
        2 = 2 * 4
        3 = 6
        [24]
        suf = [24, 12, 4, 1]
        pre = [1, 1, 2, 6]
        '''
        pre = [1]
        for i in range(len(nums) - 1):
            pre.append(nums[i] * pre[-1])
        suf = 1
        for i in range(len(nums) - 1, -1, -1):
            pre[i] = suf * pre[i]
            suf *= nums[i]
        return pre