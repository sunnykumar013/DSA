def products(arr1):
    print(arr1)

    n = len(arr1)
    prefix = [0]*n
    postfix =[0]*n
    prefix[0] = 1
    postfix[n-1] = 1
    for i in range(1,n):
        prefix[i] = arr1[i-1] * prefix[i-1]

    for i in range(n-2,-1,-1):
        postfix[i] = arr1[i+1] * postfix[i+1]

    arr1[0] = postfix[0]
    arr1[n-1] = prefix[n-1]

    for i in range(1, n-1):
        arr1[i] = prefix[i] * postfix[i]

    print("prefix ",prefix)
    print("postfix ",postfix)
    print("result", arr1)

arr =[1,2,3,4]
products(arr)