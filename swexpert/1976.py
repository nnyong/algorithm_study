T=int(input())
for test_case in range(1,T+1):

    h1,m1,h2,m2=map(int,input().split())
    new_h=h1+h2
    new_m=m1+m2
    if new_h>12:
        new_h-=12
    if new_m>=60:
        new_m-=60
        new_h+=1

    print(f'#{test_case} {new_h} {new_m}')