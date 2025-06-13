class Solution:
    def twoSum( nums: list[int], target: int) -> list[int]:
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    print(i)
                    print(j)
                    return [i, j]
        return []
print(Solution.twoSum([1,2,3,4,5],5))
#求两数相加