import sys
def main():
    testData = sys.stdin.readlines()
    
    n = int(testData[2][4:])

    fM = [i for i in range(1, n + 1)]
    wife = [0] * n
    husband = [0] * n

    mP = []
    fP = []
    invl = [0] * n

    for i in range(4, 2*n + 4, 2):
        new = list(map(int, (testData[i].split())[1:]))
        mP.append([int(i/2) for i in new])
    
    for i in range(5, 2*n + 4, 2):
        l = list(map(int, (testData[i].split())[1:]))
        for i in range(n):
            invl[int((l[i]-1)/2)] = i+1
        fP.append(invl)
        invl = [0] * n
    
    while fM:
        m = fM[0]
        for w in mP[m-1]:
            mP[m-1].pop(0)
            if husband[w-1] == 0:
                wife[m-1] = w
                husband[w-1] = m
                fM.pop(0)
                break
            m2 = husband[w-1]
            if fP[w-1][m-1] < fP[w-1][m2-1]:
                wife[m2-1] = 0
                wife[m-1] = w
                husband[w-1] = m
                fM.pop(0)
                fM.insert(0, m2)
                break
    for i in range(0, n):
        print(i*2+1, wife[i]*2)
main()


    
