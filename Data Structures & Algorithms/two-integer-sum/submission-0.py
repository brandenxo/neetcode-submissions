class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for index, n in enumerate(nums):
            if n in hash_map:
                return [hash_map[n], index]

            hash_map[target - n] = index