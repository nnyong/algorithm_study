T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    k=0
    l=[]
    while l!=[0,1,2,3,4,5,6,7,8,9]:
        k+=1
        for i in str(n*k):
            if int(i) not in l:
                l.append(int(i))
                l.sort()
    print(f'#{test_case} {n*k}')