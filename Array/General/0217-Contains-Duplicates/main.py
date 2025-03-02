def containsDuplicate(nums: list[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True