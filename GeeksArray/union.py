def unionIn(arr1,arr2):
     i=0
     j=0
     m =len(arr1)
     n =len(arr2)
     reslst=[]
     intersectLst=[]
     while i<m and j<n:
          if(arr1[i] < arr2[j]):
               reslst.append(arr1[i])
               i += 1

          elif arr1[i] > arr2[j]:
               reslst.append(arr2[j])
               j +=1

          else:
               reslst.append((arr1[i]))
               intersectLst.append(arr1[i])
               i += 1
               j += 1

     while i<m:
          reslst.append(arr1[i])
          i +=1

     while j< n:
          reslst.append(arr2[j])
          j += 1

     print(reslst)
     print(intersectLst)









arr3=[1, 3, 4, 5, 7]
arr4=[2, 3, 5, 6]
unionIn(arr3, arr4)