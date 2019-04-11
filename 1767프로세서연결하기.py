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

    visited=[[0]*n for _ in range(n)]
    def connect(begin_y,begin_x,core=0,length=0):
        global max_core,min_len
        flag=0
        cnt=0
        for y in range(begin_y+1,n-1):
            for x in range(begin_x+1,n-1):
                if data[y][x]==1 and not visited[y][x]:
                    visited[y][x]=1
                    for dir in range(5):
                        newy=y+dy[dir]
                        newx=x+dx[dir]
                        while isSafe(newy,newx):
                            if visited[newy][newx]==1:
                                while True:
                                    newy-=dy[dir]
                                    newx-=dx[dir]
                                    if newy==y and newx==x:
                                        break
                                    visited[newy][newx]=0
                            if data[newy][newx]==0 and not visited[newy][newx]:
                                visited[newy][newx]=1
                                for v in visited:
                                    print(v)
                                print('-------------------------')
                                newy+=dy[dir]
                                newx+=dx[dir]
                                cnt+=1
                                flag=1
                            else:
                                break
                        if flag==1:
                            connect(y,x,core + 1, length + cnt)
                            while True:
                                newy -= dy[dir]
                                newx -= dx[dir]
                                if newy == y and newx == x:
                                    break
                                visited[newy][newx] = 0
        if core<max_core:
            return
        if length>min_len:
            return
        if core>max_core:
            max_core=core
        if length<min_len:
            min_len=length
        return


    max_core=0
    min_len=987654321
    connect(0,0)
    print(min_len)