
def contiguousSum(arr1):

    max_so_far = -123456
    max_end_here =0
    # lst1=[]
    # startend=9876543221
    # endindex=0
    for i in range(len(arr1)):

        max_end_here += arr1[i]

        if(max_end_here>max_so_far):

            max_so_far = max_end_here

        if(max_end_here<0):

            max_end_here=0


    print(arr1)
    print(max_so_far)
    # print(startend,endindex)


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
arr2=[-2,1,-3,4,-1,2,1,-5,4]
contiguousSum(arr2)