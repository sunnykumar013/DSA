class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        lis = [1] * len(nums)
        n = len(nums)
        print(lis)

        for i in range(1,n):
            for j in range(0, i):
                if nums[i] > nums[j] and lis[j] +1 > lis[i]:
                    lis[i] = lis[j] +1


        return max(lis)