# 프로세스연결하기
import sys
sys.stdin=open('프로세서','r')

def isSafe(y, x):
    if y >= 0 and y < n and x >= 0 and x < n:
        return True
    else:
        return False

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(map(int,input().split())) for _ in range(n)]
    # print(data)

    dy=[-1,0,1,0,0]
    dx=[0,-1,0,1,0]