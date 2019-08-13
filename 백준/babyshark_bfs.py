# 아기상어 bfs
import sys
sys.stdin=open('아기상어','r')

# T=int(input())
# for tc in range(1,T+1):

def isSafe(y,x):
    if y<n and y>=0 and x<n and x>=0:
        return True
    else:
        return False
def findbaby():
    global by,bx
    for y in range(n):
        for x in range(n):
            if data[y][x]==9:
                by=y
                bx=x
                return

def shark(y,x,size):
    flag=0
    min_location=(n-1,n-1)
    data[y][x] = 0
    queue.append((y,x))
    dis = 0
    while queue:
        for i in range(len(queue)):
            new=queue.pop(0)
            for dir in range(4):
                new_y = new[0]+dy[dir]
                new_x = new[1]+dx[dir]
                if isSafe(new_y,new_x) and not visited[new_y][new_x]:
                    if data[new_y][new_x]<=size:
                        visited[new_y][new_x]=1
                        if data[new_y][new_x]<size and data[new_y][new_x]!=0:
                            if flag==0:
                                min_location=(new_y,new_x)
                                flag=1
                            else:
                                if new_y<min_location[0]:
                                    min_location=(new_y,new_x)
                                elif new_y==min_location[0]:
                                    if new_x<min_location[1]:
                                        min_location=(new_y,new_x)
                        queue.append((new_y,new_x))
            # print(queue)
        dis+=1
        if flag==1:
            data[min_location[0]][min_location[1]] = 9
            return dis
    return False
        # print(dis)
n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
dy=[-1,0,0,1]
dx=[0,-1,1,0]
result=0
size = 2
eat=0
while True:
    by=bx=0
    findbaby()
    queue=[]
    visited=[[0]*n for _ in range(n)]
    visited[by][bx]=1
    d=shark(by,bx,size)
    if not d:
        break
    else:
        eat+=1
    if eat==size:
        size+=1
        eat=0
    result+=d
print(result)