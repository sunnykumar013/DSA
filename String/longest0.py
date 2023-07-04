#s = "esdffd0000000000hdgff0000000000000gfcxgfcgc00000"

def longZero(s):
    # s = input("Enter the string:")
    longest_len = 0
    count = 0
    for i in s:
        if i=="0":
            count+=1
        else:
            if longest_len<count:
                longest_len = count
            count = 0

    print(longest_len)

longZero("esdffd0000000000hdgff0000000000000gfcxgfcgc00000")
