# 소인수분해
T=int(input())
for test_case in range(1,T+1):
    n=int(input())
    d={2:0,3:0,5:0,7:0,11:0}
    while n!=1:
        for i in d.keys():
            if n%i==0:
                d[i]+=1
                n/=i
                break
    print(f'#{test_case}', end=" ")
    for i in d.values():
        print(i,end=" ")
    print()
