T=int(input())
for tc in range(1,T+1):
    n=int(input())

    sum=0
    for i in range(1,n+1):
        if i%2==0:
            sum-=i
        else:
            sum+=i

    print(f'#{tc} {sum}')