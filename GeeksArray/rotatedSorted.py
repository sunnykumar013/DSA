def search( nums, target):
    l = 0
    r = len(nums) - 1

    while (l <= r):

        mid = int((l + r) / 2)

        if (nums[mid] == target):
            return mid

        if (nums[mid] >= nums[l]):

            if (target >= nums[l] and target <= nums[mid]):
                r = mid - 1

            else:
                l = mid + 1

        else:

            if (target >= nums[mid] and target <= nums[r]):
                l = mid + 1

            else:
                r = mid - 1

    return -1

arr =[ 4, 5, 6, 7, 8, 9, 1, 2, 3]
print(search(arr, 8))