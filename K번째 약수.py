W = 0
A = 1
N , K= map(int,input("숫자을 입력해주세요").split())
if((N>=1 and N<=10000) and (K >= 1 and K <= N)) :
    while A <= N :
        if (N % A == 0) :
            W+=1
            if W == K :
                print(A)
                break
        A+=1
else :
	print(-1)