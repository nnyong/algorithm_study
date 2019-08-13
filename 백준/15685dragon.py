# 드래곤커브
import sys
sys.stdin=open("드래곤.txt",'r')

n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]

visited=[[0]*101 for _ in range(101)]

dy=[0,-1,0,1]
dx=[1,0,-1,0]

dir0=[[0,1],[2,1],[2,3],[0,3]]
dir1=[[1,2],[3,2],[3,0],[1,0]]
dir2=[[2,3],[0,3],[0,1],[2,1]]
dir3=[[3,0],[1,0],[1,2],[3,2]]
dir=[dir0,dir1,dir2,dir3]

for i in range(n):
    x,y,d,g=list(data[i])
    py=y
    px=x
    visited[py][px]=1
    li=[]
    if g==0:
        py=py+dy[d]
        px=px+dx[d]
        visited[py][px]=1
    else:
        for r in range(g):
            if r==0:
                li.append(0)
            else:
                for l in range(len(li)-1, -1, -1):
                    if li[l]==3:
                        next=0
                    else:
                        next=li[l]+1
                    li.append(next)

        for l in li:
            for j in range(2):
                py=py+dy[dir[d][l][j]]
                px=px+dx[dir[d][l][j]]
                visited[py][px]=1

def count():
    cnt=0
    for y in range(100):
        for x in range(100):
            if visited[y][x]==1 and visited[y][x+1]==1 and visited[y+1][x]==1 and visited[y+1][x+1]==1:
                cnt+=1
    return cnt

result=count()
print(result)