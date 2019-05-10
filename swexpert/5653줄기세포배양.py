import sys
sys.stdin=open('줄기세포.txt','r')

T=int(input())
for tc in range(1,T+1):
    print('#{}'.format(tc))
    n,m,k=map(int,input().split())
    data=[list(map(int,input().split())) for _ in range(n)]
    print(data)

    cell=[[0]*(m+k) for _ in range(n+k)]
    print(cell)
    visited=[[0]*(m+k) for _ in range(n+k)]