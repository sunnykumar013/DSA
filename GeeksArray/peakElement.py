# def peak(arr1):
#     print(arr1)
#     n = len(arr1)
#     if(arr1[0] > arr1[1]):
#         print(arr1[0])
#
#     if(arr1[n-1] > arr1[n-2]):
#         print(arr1[n-1])
#
#     for i in range(1,n):
#         if(arr1[i] > arr1[i-1] and arr1[i] >arr1[i+1]):
#             print(arr1[i])
#

def peakEle(arr2):

    n = len(arr2)
    if(arr2[0] > arr2[1]):
        print(arr2[0])

    if(arr2[n-1] > arr2[n-2]):
        print(arr2[n-1])

    l = 0
    r =n - 1
    while(l <= r):
        mid = (l + r) // 2

        if(arr2[mid] > arr2[mid+1] and arr2[mid] > arr2[mid - 1]):
            print(arr2[mid])
            l = mid + 1
            # r = mid - 1

        elif(arr2[mid]< arr2[mid-1]):
            r =mid-1

        elif(arr2[mid]> arr2[mid+1]):
            l = mid + 1





arr =[10, 20, 15, 2, 23, 90, 67]
peakEle(arr)