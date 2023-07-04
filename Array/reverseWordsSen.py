def revw(s1):
    sl1 = list(s1)
    i =0
    j = len(sl1) -1
    while(i<=j):
        sl1[i], sl1[j] = sl1[j], sl1[i]

        i = i+1
        j = j -1

        s1 = "".join(sl1)
    # print(s1)

    return s1


def rev(s1):
    print(s1)

    sl1 = s1.split(' ')

    li =[]

    for i in range(len(sl1)):
        # print(type(revw(sl1[i])))
        li.append(revw(sl1[i]))

    revs = li[-1::-1]

    revws =" ".join(revs)

    print(revws)


    # print(li)


    # sl1 = li[-1::-1]

    # s1 =' '.join(li)
    # print(li)






rev("she likes this program very much")