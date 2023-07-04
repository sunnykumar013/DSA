# solution from gfg

def lisub(arr):
    n = len(arr)
    lis = [1] * n
    print(lis)

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis[j] + 1 > lis[i]:
                lis[i] = lis[j] + 1

    return max(lis)


arr1 = [10, 9, 2, 5, 3, 7, 101, 18]
print(lisub(arr1))
