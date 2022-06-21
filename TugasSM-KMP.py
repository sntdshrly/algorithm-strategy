def cfail(pola):
    fail = [None] * len(pola)
    fail[0]=0
    m = len(pola)
    j = 0
    i = 1
    #while . . .
    while (i < m): 
        if (pola[j] == pola[i]) :
            #j+1 chars match 
            fail[i] = j + 1
            i= i+1
            j= j+1
        elif (j > 0): 
            # j follows matching prefix
            j = fail[j-1];  
        else: # no match
            fail[i] = 0
            i= i+1
    return fail

def searchKMP(T,P):
    fail = cfail(P)
    n = len(T)
    m = len(P)
    i = 0
    j = 0 
    Found = False
    #while ……
    while (i < n) and (not Found):
        if (P[j] == T[i]):
            if (j == m-1):
                Found = True
                hasil = i-m+1
            else: 
                j = j + 1
                i = i + 1
        elif (j > 0): 
            print("i=",i)
            print(f'j= F({j-1})= ',end="")
            j = fail[j-1]
            print(f'{j}')
        else:
            i = i + 1
            print("i=",i)
            print(f'j= {j}')
    if (not Found):
        hasil = -1
    return hasil

def main():
    T = str(input("Teks:"))
    P = str(input("Pola:"))
    print(searchKMP(T,P))
if __name__ == '__main__':
    main()