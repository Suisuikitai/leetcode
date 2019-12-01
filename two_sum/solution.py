from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for index in range(len(nums)):
            elem = target - nums[index]
            if nums[index] not in ans:
                ans[nums[index]] = index
            if elem in ans and index != ans[elem]:
                return [index, ans[elem]]
