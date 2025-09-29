class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0 and nums[i-1] % 2 == 0:
                return False
            elif nums[i] % 2 != 0 and nums[i-1] % 2 != 0:
                return False
        return True

# checking equal parity of neighbors in array
