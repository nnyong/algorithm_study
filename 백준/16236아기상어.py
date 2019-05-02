import sys
sys.stdin=open('아기상어','r')

# T=int(input())
# for tc in range(1,T+1):
n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
def isSafe(y,x):
    if y<n and y>=0 and x<n and x>=0:
        return True
    else:
        return False

dy=[-1,0,0,1]
dx=[0,-1,1,0]

def findbaby():
    global by,bx
    for y in range(n):
        for x in range(n):
            if data[y][x]==9:
                by=y
                bx=x
                return

def shark(y,x,size,dis=0):
    global min_dis,result,by,bx,min_x,min_y,flag
    if dis>min_dis:
        return
    if data[y][x]<size and data[y][x]!=0:
        if dis<=min_dis:
            if dis==min_dis:
                if y<min_y:
                    min_dis=dis
                    min_y=y
                    min_x=x
                    return
                elif y==min_y:
                    if x<min_x:
                        min_dis = dis
                        min_y = y
                        min_x = x
                        return
            else:
                min_dis = dis
                min_y = y
                min_x = x
                return
    if data[y][x]==9:
        data[y][x]=0
    for dir in range(4):
        new_y=y+dy[dir]
        new_x=x+dx[dir]
        if isSafe(new_y,new_x) and data[new_y][new_x]<=size and not visited[new_y][new_x]:
            # visited[new_y][new_x]=1
            # if data[new_y][new_x]<size and data[new_y][new_x]!=0:
            #     if dis+1<min_dis:
            #         min_dis=dis+1
            #         min_y=new_y
            #         min_x=new_x
            #         visited[min_y][min_x]=0
            #         return
            visited[new_y][new_x] = 1
            shark(new_y,new_x,size,dis+1)
            visited[new_y][new_x] = 0
    if y==by and x==bx:
        print(min_y,min_x)
        if min_y==n and min_x==n:
            flag=0
            return
        data[min_y][min_x]=9
        return

size=2
eat=0
result=0
while True:
    flag=1
    by = bx = 0
    visited = [[0] * n for _ in range(n)]
    findbaby()
    visited[by][bx]=1
    min_dis=987654321
    min_y = n
    min_x = n
    shark(by,bx,size)

    if min_dis==987654321:
        break

    eat+=1
    if size==eat:
        size+=1
        eat=0
    # print('size:{}, eat:{}'.format(size,eat))
    # print(min_dis)
    result+=min_dis
    # print(result)
    if flag==0:
        break
print(result)


