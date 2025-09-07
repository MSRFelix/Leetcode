class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]], i]
            hashmap[nums[i]] = i

# time complexity = O(n), space complexity as well
