def findMin( nums):
    l = 0
    r = len(nums) - 1
    mini = nums[0]

    while l <= r:

        if (nums[l] < nums[r]):
            mini = min(mini, nums[l])
            return mini

        mid = (l + r) // 2
        mini = min(mini, nums[mid])
        if (nums[mid] >= nums[l]):

            l = mid + 1

        else:

            r = mid - 1

    return mini

arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
print(findMin(arr))