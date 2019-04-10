import sys
sys.stdin=open('아기상어','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(map(int,input().split())) for _ in range(n)]
    print(data)
    def isSafe(y,x):
        if y<n and y>=0 and x<n and x>=0:
            return True
        else:
            return False

    dy=[-1,0,1,0]
    dx=[0,-1,0,1]

    def findbaby():
        global by,bx
        for y in range(n):
            for x in range(n):
                if data[y][x]==9:
                    by=y
                    bx=x
                    return

    def shark(y,x,size,cnt=0):
        global time


        for dir in range(4):
            new_y=y+dy[dir]
            new_x=x+dx[dir]
            if isSafe(new_y,new_x) and data[new_y][new_x]<=size:
                time+=1
                if data[new_y][new_x]<size:
                    cnt+=1
                if cnt==size:
                    size+=1
                shark(new_y,new_x,size,cnt)

    by=bx=0
    findbaby()
    time=0
    shark(by,bx,2)
    print(time)


