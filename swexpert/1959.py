T=int(input())
for test_case in range(1,T+1):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=[]
  
    if n<=m:
        for i in range(m-n+1):
            sum=0
            for j in range(n):
                sum+=a[j]*b[i+j]
            l.append(sum)
    else:
        for i in range(n-m+1):
            sum=0
            for j in range(m):
                sum+=b[j]*a[i+j]
            l.append(sum)

    print(f'#{test_case} {max(l)}')