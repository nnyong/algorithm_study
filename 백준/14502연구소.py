import sys
from itertools import combinations
sys.stdin=open('연구소.txt','r')

n,m=list(map(int,input().split()))
data=[list(map(int,input().split())) for _ in range(n)]
# print(data)

def comb():
    li=[]
    for y in range(n):
        for x in range(m):
            if data[y][x]==0:
                li.append((y,x))
            elif data[y][x]==2:

    return list(combinations(li,3))

li0=comb()
print(li0)

def virus():
