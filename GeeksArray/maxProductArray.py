
def maxProduct(nums) :
    max_so_far = max(nums)
    max_end_here = 1
    min_end_here = 1

    for i in range(len(nums)):

        if nums[i] == 0:
            max_end_here = 1
            min_end_here = 1
            continue
        tem = max_end_here * nums[i]

        max_end_here = max(max_end_here * nums[i], min_end_here * nums[i], nums[i])
        min_end_here = min(tem, min_end_here * nums[i], nums[i])

        max_so_far = max(max_so_far, max_end_here)

    return max_so_far

arr1 =[1,0,-1,2,3,-5,-2]

print(maxProduct(arr1))