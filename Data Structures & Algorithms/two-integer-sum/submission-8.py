class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index, val in enumerate(nums):
            diff = target - val

            if diff in hashmap:
                return [hashmap[diff], index]
            else:
                hashmap[val] = index
        return []            
  