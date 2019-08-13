# 연구소
import sys,copy
from itertools import combinations

sys.stdin=open("연구소.txt",'r')

n,m=list(map(int,input().split()))
data=[list(map(int,input().split())) for _ in range(n)]

dy=[0,1,0,-1]
dx=[1,0,-1,0]

def isSafe(y,x):
    if y<n and y>=0 and x<m and x>=0:
        return True
    else:
        return False

def comb():
    global que
    li=[]
    for y in range(n):
        for x in range(m):
            if data[y][x]==0:
                li.append((y,x))
    return list(combinations(li,3))

def clean():
    cnt=0
    for y in range(n):
        for x in range(m):
            if visited[y][x]==0:
                cnt+=1
    return cnt

def queReset():
    for y in range(n):
        for x in range(m):
            if data[y][x]==2:
                que.append((y,x))
que=[]
li0=comb()
visited=copy.deepcopy(data)
result=0
for l in li0:
    for w in l:
        visited[w[0]][w[1]]=1
    queReset()
    temp_result=0
    while que:
        virus=que.pop()
        for dir in range(4):
            new_y=virus[0]+dy[dir]
            new_x=virus[1]+dx[dir]
            if isSafe(new_y,new_x) and not visited[new_y][new_x] :
                visited[new_y][new_x]=2
                que.append((new_y,new_x))
    temp_result=clean()
    if temp_result>=result:
        result=temp_result
    visited=copy.deepcopy(data)

print(result)