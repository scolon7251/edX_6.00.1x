def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        print i
        while j < len(L):
            if L[i] > L[j]:
                print i
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
            print L