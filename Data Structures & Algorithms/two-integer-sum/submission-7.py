class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []

        for index, val in enumerate(nums):
            A.append([val, index])

        A.sort()

        l, r = 0, len(nums) - 1

        while l < r:
            if A[l][0] + A[r][0] == target:
                return [min(A[l][1], A[r][1]), 
                    max(A[l][1], A[r][1])]
            elif A[l][0] + A[r][0] > target:
                r -= 1
            elif A[l][0] + A[r][0] < target:  
                l += 1

        return []    