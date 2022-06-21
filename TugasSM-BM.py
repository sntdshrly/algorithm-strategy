def lastO(pola):
    last = [None]*128
    for i in range(0,128,1):
        last[i] = -1
    for i in range(0, len(pola), 1):
        last[ord(pola[i])] = i
    return last

def searchBM(T,P):
    last = lastO(P)
    n = len(T)
    m = len(P)
    i = m-1
    if (i > n-1):
        #pola > text
        hasil = -1
    else:
        j = m-1
        Found = False
    # while ...
    while (i < n) and (not Found):
        if (P[j] == T[i]):
            if (j == 0):
                Found = True
            else:
                j = j - 1
                i = i - 1
        else: #character jump
            lo = last[ord(T[i])]
            print("lo=",lo,end=" ")
            i = i + m - min(j,1+lo)
            print("i=",i,end=" ")
            j = m-1 
            print("j=",j)
    if (Found):
        hasil = i
    else:
        hasil = -1
    return hasil

def main():
    T = str(input("Teks:"))
    P = str(input("Pola:"))
    print(searchBM(T,P))
 
if __name__ == '__main__':
    main()