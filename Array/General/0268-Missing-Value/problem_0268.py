def missingNumber(nums: list[int]) -> int:
        return sum([i for i in range(len(nums) + 1)]) - sum(nums)