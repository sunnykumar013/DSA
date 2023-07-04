def binarySearch(arr, l, r, key):

    if r >= l:
        mid = (l+r)//2
        if arr[mid] == key:
            return mid

        elif key > arr[mid]:
            return binarySearch(arr, mid+1, r, key)

        else:
            return binarySearch(arr, l, mid-1, key)
    else:
        return -1


arr = [2, 3, 4, 10, 40]
r = binarySearch(arr, 0, len(arr)-1, 400)
if r != -1:
    print("found")

else:
    print("not")