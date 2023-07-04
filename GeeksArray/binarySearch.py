# def bSearch(arr, key):
#
#     l=0
#     r=len(arr) -1
#     while l<=r:
#         mid =(l+r)//2
#         if arr[mid] == key:
#             print("match found",mid)
#             break
#
#         elif arr[mid] > key:
#             r = mid -1
#
#         else:
#             l = mid+1
#
#
#     print(arr)


#
# arr =[12,21,23,45,56,76,98]
#
# bSearch(arr,56)


def bSearch(arr,l,r,key):

    mid = (l+r)//2
    if(arr[mid] == key):
        print("match found",mid)

    elif(arr[mid] > key):
        bSearch(arr,l,mid-1,key)

    else:
        bSearch(arr,mid+1,r,key)

    # print(arr)


arr1=[12,21,23,45,56,76,98]

bSearch(arr1, 0, len(arr1)-1, 56)