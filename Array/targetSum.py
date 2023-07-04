class Solution:
    def twoSum(self, nums, target ):
        hash_map ={}

        for i in range(len(nums)):
           res = target - nums[i]

           if res in hash_map:
               return [hash_map[res], i]

           hash_map[nums[i]] = i